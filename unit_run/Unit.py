from utils import find_callable_by_name, get_info_dict_from_callable
import os, shutil, json
from glob import glob

class Unit:
    def __init__(self, unit_path, unit_name):
        self.meta = {
            'unit_path': unit_path,
            'unit_name': unit_name
        }
        self.unit = find_callable_by_name(unit_path, unit_name)
        if self.unit is None:
            raise LookupError(f"Cannot find the unit '{unit_name}' in {unit_path}.")
        self.param_group_map = dict()
        
    @classmethod
    def _load_from_json(cls, json_path):
        with open(json_path) as f:
            return json.load(f)

    @classmethod
    def _save_as_json(cls, json_path, data):
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)

    def save(self, save_dir, verbose=True):
        if os.path.isdir(save_dir):
            shutil.rmtree(save_dir)
        os.mkdir(save_dir)
        self._save_as_json(os.path.join(save_dir, '.meta.json'), self.meta)
        for group_name, group in self.param_group_map.items():
            self._save_as_json(os.path.join(save_dir, f'{group_name}.param_group.json'), group)
        if verbose:
            print(f'{len(self.param_group_map)} groups of paramters saved in {save_dir}')

    def set_param_group(self, name, group):
        self.param_group_map[name] = group

    @classmethod
    def load_from_dir(cls, load_dir, verbose=True):
        meta = cls._load_from_json(os.path.join(load_dir, '.meta.json'))
        assert 'unit_path' in meta and 'unit_name' in meta
        unit = cls(meta['unit_path'], meta['unit_name'])

        json_paths = glob(os.path.join(load_dir, '*.param_group.json'))
        for path in json_paths:
            unit.set_param_group(os.path.basename(path).replace('.param_group.json', ''), cls._load_from_json(path))
        if verbose:
            print(f"Find {len(unit.param_group_map)} groups of paramters for '{unit.meta['unit_name']}' unit in {unit.meta['unit_path']}")
        return unit

    def run(self, group_name):
        group = self.param_group_map[group_name]
        return self.unit(**group) if type(group) == dict else self.unit(*group)
    

    @property
    def unit_info(self):
        return get_info_dict_from_callable(self.unit)
    
    def __str__(self):
        new_meta = self.unit_info
        new_meta['path'] = self.meta['unit_path']
        return json.dumps({
            'meta': self.unit_info,
            'param_group_map': self.param_group_map
        }, indent=2)
    # @classmethod
    # load_from_dir

# # Create from in-memory data
# unit_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/test.py'
# unit_name = 'y'
# unit = Unit(unit_path, unit_name)
# print(unit)

# # add parameter group
# unit.set_param_group('test1', [8, 10])
# unit.set_param_group('test2', {'a': 11, 'b': 11})

# # Save at a directory
# save_dir = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/test'
# unit.save(save_dir)

# print(unit.run('test2'))

# Load unit
# load_dir = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/test'
# unit = Unit.load_from_dir(load_dir)
# unit.set_param_group('test4', [66, 11])
# print(unit)
# unit.save(load_dir)
# print(unit.run('test4'))