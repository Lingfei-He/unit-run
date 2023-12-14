from abc import ABC, abstractmethod, abstractclassmethod
from pathlib import Path
import os, sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..')))
from unit_run.utils import PathType, save_as_json, load_json, auto_type_check, get_info_dict_from_callable, find_callable_by_name
import shutil, os, json

class Base(ABC):
    PATH_TYPE = PathType.BOTH

    def __init__(self):
        self.load_path = None

    @abstractclassmethod
    def check_data(cls, data):
        pass

    def validate_data(cls, *args, **kwargs):
        try:
            cls.check_data(*args, **kwargs)
            return True
        except:
            return False

    def check(self):
        self.check_data(self)

    @property
    def valid(self):
        try:
            self.check()
            return True
        except:
            return False

    @classmethod
    def _check_file_name(cls, file_name):
        pass
    
    @classmethod
    def _check_path_to_load(cls, load_path):
        path = Path(load_path).resolve()
        if not path.exists():
            raise FileNotFoundError(f"'{path}' doesn't exists for loading")
        elif cls.PATH_TYPE == PathType.FILE and not path.is_file():
            raise FileNotFoundError(f'There is no such a file to load: {path}')
        elif cls.PATH_TYPE == PathType.DIRECTORY and not path.is_dir():
            raise FileNotFoundError(f'There is no such a directory to load: {path}')
        cls._check_file_name(path.name)

    @classmethod
    def _check_before_load(cls, load_path):
        cls._check_path_to_load(load_path)
        
    @abstractclassmethod
    def _load_raw_data(cls, load_path):
        pass

    @classmethod
    def _check_after_load(cls, raw_data):
        pass

    @classmethod
    def is_path_loadable(cls, load_path):
        try:
            cls._check_before_load(load_path)
            cls._check_after_load(cls._load_raw_data(load_path))
            return True
        except:
            return False

    @classmethod
    def _create_obj_by_raw_data(cls, raw_data):
        return cls(raw_data)

    def _update(self, other_obj):
        other_t, self_t = type(other_obj), type(self)
        if not issubclass(other_t, self_t):
            raise TypeError(f"The class '{other_t.__name__}' of  the other object is not the subclass of '{self_t.__name__}'.") 
        for attr_name, attr_value in vars(self).items():
            setattr(self, attr_name, getattr(other_obj, attr_name))
    

    @classmethod
    def load_from_disk(cls, load_path):
        cls._check_before_load(load_path)
        raw_data = cls._load_raw_data(load_path)
        cls._check_after_load(raw_data)
        new_obj = cls._create_obj_by_raw_data(raw_data)
        new_obj.load_path = load_path
        return new_obj
    
    @classmethod
    def valid_path_exists(cls, path): # should not validate the internal data to load
        try:
            cls._check_path_to_load(path)
            return True
        except:
            return False
    
    def _check_before_save(self, save_path):
        path = Path(save_path).resolve()
        if not path.parent.is_dir():
            raise FileNotFoundError(f"The parent directory to save doesn't exist: {path.parent}")
        elif self.valid_path_exists(str(path)):
            raise FileExistsError(f'{path} has already existed and cannot be overwritten.')
        self._check_file_name(path.name)

    @abstractmethod        
    def _save(self, save_path):
        pass
        # if 
    def _after_save(self, save_path):
        self.load_path = save_path

    @classmethod
    def _exist_handler(cls, path):
        path = Path(path)
        os.remove(str(path)) if path.is_file() else shutil.rmtree(path)

    def save_to_disk(self, save_path, all_overwrite=True):
        try:
            self._check_before_save(save_path)
        except FileExistsError as e:
            if all_overwrite:
                self._exist_handler(save_path)
            else:
                raise e
        self._save(save_path)
        self._after_save(save_path)

    def to_dict(self):
        return self.__dict__
    
    def to_info_dict(self):
        result = self.to_dict()
        result['valid'] = self.valid
        return result
    
    def __str__(self) -> str:
        return json.dumps(self.to_info_dict(), indent=2)
    

class Meta(Base):
    FILE_NAME = '.meta.json'
    PATH_TYPE = PathType.FILE

    @auto_type_check
    def __init__(self, src_path: str, src_name: str):
        self.src_path = src_path
        self.src_name = src_name
        super().__init__()

    @classmethod
    def check_data(cls, *param, **kwargs):
        if len(param) == 1:
            meta = param[0]
            t = type(meta)
            if t == Meta:
                if not (hasattr(meta, 'src_path') and hasattr(meta, 'src_name')):
                    raise ValueError(f'Invalid Meta Object: {meta.to_dict()}.')
            elif t == dict:
                if not ('src_path' in meta and 'src_name' in meta):
                    raise KeyError(f'Invalid dict for Meta: {meta}.')
            elif t == str or t == Path:
                path = Path(str(meta))
                if not path.is_file():
                    raise FileNotFoundError(f"Meta file '{path.resolve()}' doesn't exist.")
                elif path.suffix != Path(cls.FILE_NAME).suffix:
                    raise TypeError(f"Invalid file type: '{path.suffix}' (need '{Path(cls.FILE_NAME).suffix}').")
                else:
                    try:
                        json_data = load_json(path)
                        cls.check(json_data)
                    except:
                        raise ValueError(f"Invalid Json data read from '{path.resolve()}': {json_data}.")
        elif len(param) == 2:
            cls.check(dict(src_path=param[0], src_name=param[1]))
        elif len(param) > 2:
            raise ValueError(f'Too many positional arguments for Meta: {len(param)} (need 2).')
        else:
            if len(kwargs.keys()) == 0:
                raise ValueError(f"There is no positional argument or keyword argument.")
            if len(kwargs.keys()) > 0:
                cls.check(kwargs)

    @classmethod
    def get_path_by_dir(cls, meta_dir):
        return str(Path(meta_dir).joinpath(cls.FILE_NAME).resolve())
            

    @classmethod
    def property(cls, func):
        def getter(self):
            return getattr(self.meta, func.__name__)
        
        def setter(self, new_v):
            setattr(self.meta, func.__name__, new_v)
        return property(getter, setter)
    
    @classmethod
    def _check_file_name(cls, file_name):
        path = Path(file_name)
        target_suffix = Path(cls.FILE_NAME).suffix
        if path.suffix != target_suffix:
            raise TypeError(f"The file type is not '{target_suffix}'.")
        elif path.name != cls.FILE_NAME:
            raise NameError(f"The file name should be '{cls.FILE_NAME}', not '{path.name}'.")
    
    @classmethod
    def _load_raw_data(cls, load_path):
        return load_json(load_path)
    
    @classmethod
    def _check_after_load(cls, raw_data):
        if type(raw_data) != dict:
            raise TypeError(f"The type of meta's raw data should be '{dict.__name__}', not '{type(raw_data).__name__}'")
        else:
            keys_to_check = ['src_path', 'src_name']
            for key in keys_to_check:
                if key not in raw_data:
                    raise KeyError(f"The required key '{key}' of Meta is not in raw dict.")

    @classmethod
    def _create_obj_by_raw_data(cls, raw_data):
        return cls(raw_data['src_path'], raw_data['src_name'])

    def _save(self, save_path):
        data = self.to_dict()
        del data['load_path']
        save_as_json(save_path, data)
    

# meta_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/tests/test/.meta.json'
# new_meta_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/tests/.meta.json'
# meta = Meta.load_from_disk(meta_path) 
# print(meta.to_dict())
# meta.save_to_disk(new_meta_path)
# print(meta.to_dict())
# path = Path('tzffaaf.json')
# print(Path(path).suffix)

class ParameterGroup(Base):
    FILE_SUFFIX = '.param_group.json'
    PATH_TYPE = PathType.FILE

    def __init__(self, data):
        self.data = data
        super().__init__()

    @classmethod
    def check_data(cls, data):
        json.dumps(data)
    
    def check(self):
        self.check_data(self.data)

    @classmethod
    def get_file_name(cls, name):
        return name+cls.FILE_SUFFIX
    
    @classmethod
    def get_path_by_dir_and_name(cls, dir_path, name):
        return os.path.join(dir_path, cls.get_file_name(name))
    
    @classmethod
    def get_name_from_path(cls, path):
        return Path(path).name.replace(cls.FILE_SUFFIX, '')

    @classmethod
    def _check_file_name(cls, file_name):
        splits = os.path.basename(file_name).split('.')
        err_msg = f"The file suffix of parameter group should be '{cls.FILE_SUFFIX}'"
        if len(splits) <= 1:
            err_msg += ', instead empty.'
            raise NameError(err_msg)
        else:
            suffix = '.' + '.'.join(splits[-2:])
            if suffix != cls.FILE_SUFFIX:
                err_msg += f", instead '{suffix}'."
                raise NameError(err_msg)

    @classmethod
    def _load_raw_data(cls, load_path):
        return load_json(load_path)
    
    @classmethod
    def load_by_dir_and_name(cls, dir_path, name):
        return cls.load_from_disk(cls.get_path_by_dir_and_name(dir_path, name))

    def _save(self, save_path):
        save_as_json(save_path, self.data)
        
    def save_by_dir_and_name(self, dir_path, name):
        self.save_to_disk(self.get_path_by_dir_and_name(dir_path, name))
    

# dir_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/tests'
# group = ParameterGroup(None)
# print(group)
# group.save_by_dir_and_name(dir_path, 'test')
# print(group)

class Unit(Base):
    PATH_TYPE = PathType.DIRECTORY

    @Meta.property
    def src_path(self):
        pass

    @Meta.property
    def src_name(self):
        pass

    def __init__(self, src_path, src_name):
        self.meta = Meta(src_path, src_name)
        self.param_group_map = dict()
        super().__init__()

    @classmethod
    def check_data(cls, unit):
        unit.meta.check()
        for group in unit.param_group_map.values():
            group.check()
        unit.check_src_obj()

    def check_src_obj(self):
        if not Path(self.meta.src_path).exists():
            raise FileNotFoundError(f'Source not found: {self.meta.src_path}')
        src_obj = find_callable_by_name(str(Path(self.meta.src_path).resolve()), self.meta.src_name)
        if src_obj is None:
            raise LookupError(f"Cannot find the unit source '{self.meta.src_name}' from '{self.meta.src_path}'")
        else:
            return src_obj
    
    @property
    def src_obj_valid(self):
        try:
            self.check_src_obj()
            return True
        except:
            return False

    @property
    def src_obj(self):
        try:
            return self.check_src_obj()
        except:
            return None
    
    @classmethod
    def _check_path_to_load(cls, load_path):
        super()._check_path_to_load(load_path)
        sub_file_paths = Path(load_path).glob('*')
        meta_paths = list(filter(lambda path: Meta.valid_path_exists(path), sub_file_paths))
        if len(meta_paths) != 1:
            raise LookupError(f'There is no valid meta file to load.')

    @classmethod
    def _check_after_load(cls, raw_data):
        super()._check_after_load(raw_data)
        Meta.check_data(raw_data['meta'])
        for key, group in raw_data['param_group_pairs']:
            group.check()

    @classmethod
    def get_param_group_pairs_from_dir(cls, dir_path):
        return [(ParameterGroup.get_name_from_path(str(path)), ParameterGroup.load_from_disk(str(path))) for path in Path(dir_path).glob('*') if ParameterGroup.valid_path_exists(path)]

    @classmethod
    def _load_raw_data(cls, load_dir):
        meta_load_path = Meta.get_path_by_dir(load_dir)
        meta_raw_data = Meta._load_raw_data(meta_load_path)
        param_group_pairs = cls.get_param_group_pairs_from_dir(load_dir)
        return {
            'meta': meta_raw_data,
            'param_group_pairs': param_group_pairs
        }


    @classmethod
    def _create_obj_by_raw_data(cls, raw_data):
        obj = cls(raw_data['meta']['src_path'], raw_data['meta']['src_name'])
        for key, group in raw_data['param_group_pairs']:
            obj.set_param_group(key, group, with_check=False)
        return obj

    def _check_before_save(self, save_path):
        super()._check_before_save(save_path)
        self.check()

    def _save(self, save_dir):
        if not Path(save_dir).is_dir():
            os.mkdir(save_dir)
        else:
            pairs = self.get_param_group_pairs_from_dir(save_dir)
            for name, path in pairs:
                os.remove(path)
        self.meta._save(Meta.get_path_by_dir(save_dir))
        for name, group in self.param_group_map.items():
            group._save(ParameterGroup.get_path_by_dir_and_name(save_dir, name))

    def set_param_group(self, name, group, with_check=True):
        if not isinstance(group, ParameterGroup):
            group = ParameterGroup(group)
        if with_check:
            group.check()
        self.param_group_map[name] = group

    def set_param_group_from_disk(self, path, new_name=None):
        # print(ParameterGroup._load_raw_data(path))
        group = ParameterGroup(ParameterGroup._load_raw_data(path))
        if new_name is None:
            new_name = ParameterGroup.get_name_from_path(path)
        # print(new_name)
        self.set_param_group(new_name, group, with_check=False)

    def rename_param_group(self, old_name, new_name, overwrite=False):
        if new_name in self and not overwrite:
            raise NameError(f'New name for paramter group exists: {new_name}')
        if old_name not in self:
            raise NameError(f"Old name for paramter group doesn't exists: {old_name}")
        self.param_group_map[new_name] = self.param_group_map[old_name]
        del self.param_group_map[old_name]

    def run(self, group_name):
        group = self.param_group_map[group_name]
        group.check()
        params = group.data
        self.meta.check()
        self.check_src_obj()
        src_obj = self.src_obj
        return src_obj(**params) if type(params) == dict else src_obj(*params)
    
    def _get_param_group_map_dict(self):
        r = dict()
        for k, v in self.param_group_map.items():
            r[k] = v.to_info_dict()
        return r

    def to_info_dict(self, return_trace=False):
        """The information `dict` for the source unit object

        :example: 
        ```python
            print(unit)
        ```
        ```{code-block} json
        {
            "meta": {
                "src_path": "test.py",
                "src_name": "y",
                "load_path": null
            },
            "meta_valid": true,
            "src_valid": false,
            "src_obj_info": null,
            "param_group_map": {
                "name1": {
                    "data": [1, 2],
                    "load_path": "test/name1.param_group.json",
                    "valid": true
                },
                "name2": {
                    "data": [10, 1],
                    "load_path": "test/name3.param_group.json",
                    "valid": true
                }
            }
        }
        ```
        """
        src_obj = None
        try:
            src_obj = self.check_src_obj()
            src_valid = True
            src_obj_info = get_info_dict_from_callable(src_obj)
        except:
            src_valid = False
            if return_trace:
                import traceback
                 # 获取完整的Traceback
                # exc_type, exc_value, exc_traceback = sys.exc_info()
                src_obj_info = traceback.format_exc()
            else:
                src_obj_info = None

        return {
            'meta': self.meta.to_dict(),
            'meta_valid': self.meta.valid,
            'src_valid': src_valid,
            'src_obj_info': src_obj_info,
            'param_group_map': self._get_param_group_map_dict()
        }

    @property
    def src_obj_info(self):
        self.check_src_obj()
        return get_info_dict_from_callable(self.src_obj)
    
    # @property
    # def summary(self):
    #     new_meta = self.unit_info
    #     new_meta['path'] = self.src_path
    #     return {
    #         'meta': self.unit_info,
    #         'param_group_map': self.param_group_map
    #     }
# """Whether `group_name` `in` param_group_map of Unit

#         Args:
#             group_name (string): Target parameter group name

#         Returns:
#             ``bool``: Whether ``group_name`` ``in`` param_group_map of Unit

#         Example:
#             ``python
#                 unit = Unit()
#                 print('name1' in unit)
#             ``
#         """
    def __contains__(self, group_name):
        """Whether *group_name* `in` param_group_map of Unit

        :param group_name: Target parameter group name
        :return: Whether *group_name* `in` param_group_map of Unit
        :Example:
            ```python
                unit = Unit(src_path, src_name)
                print('name1' in unit)
            ```
        """
        
        return group_name in self.param_group_map


# unit_dir = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/examples/tests/test'
# unit = Unit.load_from_disk(unit_dir)
# print(unit)
# unit.save_to_disk(unit_dir)
# print(unit.run('name3'))
# src_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/examples/tests/test.py'
# src_name = 'y'

# @auto_type_check
# def func(a, b:int):
#     pass
    # print(inspect.getframeinfo(inspect.currentframe()))

# func(1, 'fdaaa')
# print(Path('test.param_group.json').stem)
# unit = Unit(src_path, src_name)
# param_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/examples/tests/manual_p_group1.json'
# unit.set_param_group_from_disk(param_path)
# unit.rename_param_group('manual_p_group1', 'example_1')
# print(unit)
# unit.save_to_disk(Path(src_path).parent.joinpath('test').resolve())
# print(unit.src_path, unit.src_name)
# unit_dir = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/tests/test.jioni.fda'
# meta = Meta('steswt', 'tes')
# print(Path(unit_dir).stem)
# print(Meta.check == meta.check_valid)
# os.path.join(load_dir, '*.param_group.json')
# print(list(Path(unit_dir).glob('*.param_group.json')))
# unit.check()
# print(unit.src_path)
# print(dir(Meta))
# meta = Meta('test.py', 'y')
# print(meta.to_dict())

# p = Path('D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/unit_run/dfafa/tils.py')
# print(list(p.parents))
# print(p)
# p2 = Path('D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/tests')
# print(p2.exists())
# print(p. == p2.resolve())

# x = [1,2,3]
# print(len(list(filter(lambda a: a>1, x))))