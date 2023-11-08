# {py:mod}`unit_run.components`

```{py:module} unit_run.components
```

```{autodoc2-docstring} unit_run.components
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Base <unit_run.components.Base>`
  -
* - {py:obj}`Meta <unit_run.components.Meta>`
  -
* - {py:obj}`ParameterGroup <unit_run.components.ParameterGroup>`
  -
* - {py:obj}`Unit <unit_run.components.Unit>`
  -
````

### API

`````{py:class} Base()
:canonical: unit_run.components.Base

Bases: {py:obj}`abc.ABC`

````{py:attribute} PATH_TYPE
:canonical: unit_run.components.Base.PATH_TYPE
:value: >
   None

```{autodoc2-docstring} unit_run.components.Base.PATH_TYPE
```

````

````{py:method} check_data(data)
:canonical: unit_run.components.Base.check_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Base.check_data
```

````

````{py:method} validate_data(*args, **kwargs)
:canonical: unit_run.components.Base.validate_data

```{autodoc2-docstring} unit_run.components.Base.validate_data
```

````

````{py:method} check()
:canonical: unit_run.components.Base.check

```{autodoc2-docstring} unit_run.components.Base.check
```

````

````{py:property} valid
:canonical: unit_run.components.Base.valid

```{autodoc2-docstring} unit_run.components.Base.valid
```

````

````{py:method} _check_file_name(file_name)
:canonical: unit_run.components.Base._check_file_name
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._check_file_name
```

````

````{py:method} _check_path_to_load(load_path)
:canonical: unit_run.components.Base._check_path_to_load
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._check_path_to_load
```

````

````{py:method} _check_before_load(load_path)
:canonical: unit_run.components.Base._check_before_load
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._check_before_load
```

````

````{py:method} _load_raw_data(load_path)
:canonical: unit_run.components.Base._load_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._load_raw_data
```

````

````{py:method} _check_after_load(raw_data)
:canonical: unit_run.components.Base._check_after_load
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._check_after_load
```

````

````{py:method} is_path_loadable(load_path)
:canonical: unit_run.components.Base.is_path_loadable
:classmethod:

```{autodoc2-docstring} unit_run.components.Base.is_path_loadable
```

````

````{py:method} _create_obj_by_raw_data(raw_data)
:canonical: unit_run.components.Base._create_obj_by_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._create_obj_by_raw_data
```

````

````{py:method} _update(other_obj)
:canonical: unit_run.components.Base._update

```{autodoc2-docstring} unit_run.components.Base._update
```

````

````{py:method} load_from_disk(load_path)
:canonical: unit_run.components.Base.load_from_disk
:classmethod:

```{autodoc2-docstring} unit_run.components.Base.load_from_disk
```

````

````{py:method} valid_path_exists(path)
:canonical: unit_run.components.Base.valid_path_exists
:classmethod:

```{autodoc2-docstring} unit_run.components.Base.valid_path_exists
```

````

````{py:method} _check_before_save(save_path)
:canonical: unit_run.components.Base._check_before_save

```{autodoc2-docstring} unit_run.components.Base._check_before_save
```

````

````{py:method} _save(save_path)
:canonical: unit_run.components.Base._save
:abstractmethod:

```{autodoc2-docstring} unit_run.components.Base._save
```

````

````{py:method} _after_save(save_path)
:canonical: unit_run.components.Base._after_save

```{autodoc2-docstring} unit_run.components.Base._after_save
```

````

````{py:method} _exist_handler(path)
:canonical: unit_run.components.Base._exist_handler
:classmethod:

```{autodoc2-docstring} unit_run.components.Base._exist_handler
```

````

````{py:method} save_to_disk(save_path, all_overwrite=True)
:canonical: unit_run.components.Base.save_to_disk

```{autodoc2-docstring} unit_run.components.Base.save_to_disk
```

````

````{py:method} to_dict()
:canonical: unit_run.components.Base.to_dict

```{autodoc2-docstring} unit_run.components.Base.to_dict
```

````

````{py:method} to_info_dict()
:canonical: unit_run.components.Base.to_info_dict

```{autodoc2-docstring} unit_run.components.Base.to_info_dict
```

````

````{py:method} __str__() -> str
:canonical: unit_run.components.Base.__str__

````

`````

`````{py:class} Meta(src_path: str, src_name: str)
:canonical: unit_run.components.Meta

Bases: {py:obj}`unit_run.components.Base`

````{py:attribute} FILE_NAME
:canonical: unit_run.components.Meta.FILE_NAME
:value: >
   '.meta.json'

```{autodoc2-docstring} unit_run.components.Meta.FILE_NAME
```

````

````{py:attribute} PATH_TYPE
:canonical: unit_run.components.Meta.PATH_TYPE
:value: >
   None

```{autodoc2-docstring} unit_run.components.Meta.PATH_TYPE
```

````

````{py:method} check_data(*param, **kwargs)
:canonical: unit_run.components.Meta.check_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta.check_data
```

````

````{py:method} get_path_by_dir(meta_dir)
:canonical: unit_run.components.Meta.get_path_by_dir
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta.get_path_by_dir
```

````

````{py:method} property(func)
:canonical: unit_run.components.Meta.property
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta.property
```

````

````{py:method} _check_file_name(file_name)
:canonical: unit_run.components.Meta._check_file_name
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta._check_file_name
```

````

````{py:method} _load_raw_data(load_path)
:canonical: unit_run.components.Meta._load_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta._load_raw_data
```

````

````{py:method} _check_after_load(raw_data)
:canonical: unit_run.components.Meta._check_after_load
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta._check_after_load
```

````

````{py:method} _create_obj_by_raw_data(raw_data)
:canonical: unit_run.components.Meta._create_obj_by_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Meta._create_obj_by_raw_data
```

````

````{py:method} _save(save_path)
:canonical: unit_run.components.Meta._save

```{autodoc2-docstring} unit_run.components.Meta._save
```

````

`````

`````{py:class} ParameterGroup(data)
:canonical: unit_run.components.ParameterGroup

Bases: {py:obj}`unit_run.components.Base`

````{py:attribute} FILE_SUFFIX
:canonical: unit_run.components.ParameterGroup.FILE_SUFFIX
:value: >
   '.param_group.json'

```{autodoc2-docstring} unit_run.components.ParameterGroup.FILE_SUFFIX
```

````

````{py:attribute} PATH_TYPE
:canonical: unit_run.components.ParameterGroup.PATH_TYPE
:value: >
   None

```{autodoc2-docstring} unit_run.components.ParameterGroup.PATH_TYPE
```

````

````{py:method} check_data(data)
:canonical: unit_run.components.ParameterGroup.check_data
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup.check_data
```

````

````{py:method} check()
:canonical: unit_run.components.ParameterGroup.check

```{autodoc2-docstring} unit_run.components.ParameterGroup.check
```

````

````{py:method} get_file_name(name)
:canonical: unit_run.components.ParameterGroup.get_file_name
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup.get_file_name
```

````

````{py:method} get_path_by_dir_and_name(dir_path, name)
:canonical: unit_run.components.ParameterGroup.get_path_by_dir_and_name
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup.get_path_by_dir_and_name
```

````

````{py:method} get_name_from_path(path)
:canonical: unit_run.components.ParameterGroup.get_name_from_path
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup.get_name_from_path
```

````

````{py:method} _check_file_name(file_name)
:canonical: unit_run.components.ParameterGroup._check_file_name
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup._check_file_name
```

````

````{py:method} _load_raw_data(load_path)
:canonical: unit_run.components.ParameterGroup._load_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup._load_raw_data
```

````

````{py:method} load_by_dir_and_name(dir_path, name)
:canonical: unit_run.components.ParameterGroup.load_by_dir_and_name
:classmethod:

```{autodoc2-docstring} unit_run.components.ParameterGroup.load_by_dir_and_name
```

````

````{py:method} _save(save_path)
:canonical: unit_run.components.ParameterGroup._save

```{autodoc2-docstring} unit_run.components.ParameterGroup._save
```

````

````{py:method} save_by_dir_and_name(dir_path, name)
:canonical: unit_run.components.ParameterGroup.save_by_dir_and_name

```{autodoc2-docstring} unit_run.components.ParameterGroup.save_by_dir_and_name
```

````

`````

`````{py:class} Unit(src_path, src_name)
:canonical: unit_run.components.Unit

Bases: {py:obj}`unit_run.components.Base`

````{py:attribute} PATH_TYPE
:canonical: unit_run.components.Unit.PATH_TYPE
:value: >
   None

```{autodoc2-docstring} unit_run.components.Unit.PATH_TYPE
```

````

````{py:method} src_path()
:canonical: unit_run.components.Unit.src_path

```{autodoc2-docstring} unit_run.components.Unit.src_path
```

````

````{py:method} src_name()
:canonical: unit_run.components.Unit.src_name

```{autodoc2-docstring} unit_run.components.Unit.src_name
```

````

````{py:method} check_data(unit)
:canonical: unit_run.components.Unit.check_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Unit.check_data
```

````

````{py:method} check_src_obj()
:canonical: unit_run.components.Unit.check_src_obj

```{autodoc2-docstring} unit_run.components.Unit.check_src_obj
```

````

````{py:property} src_obj_valid
:canonical: unit_run.components.Unit.src_obj_valid

```{autodoc2-docstring} unit_run.components.Unit.src_obj_valid
```

````

````{py:property} src_obj
:canonical: unit_run.components.Unit.src_obj

```{autodoc2-docstring} unit_run.components.Unit.src_obj
```

````

````{py:method} _check_path_to_load(load_path)
:canonical: unit_run.components.Unit._check_path_to_load
:classmethod:

```{autodoc2-docstring} unit_run.components.Unit._check_path_to_load
```

````

````{py:method} _check_after_load(raw_data)
:canonical: unit_run.components.Unit._check_after_load
:classmethod:

```{autodoc2-docstring} unit_run.components.Unit._check_after_load
```

````

````{py:method} get_param_group_pairs_from_dir(dir_path)
:canonical: unit_run.components.Unit.get_param_group_pairs_from_dir
:classmethod:

```{autodoc2-docstring} unit_run.components.Unit.get_param_group_pairs_from_dir
```

````

````{py:method} _load_raw_data(load_dir)
:canonical: unit_run.components.Unit._load_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Unit._load_raw_data
```

````

````{py:method} _create_obj_by_raw_data(raw_data)
:canonical: unit_run.components.Unit._create_obj_by_raw_data
:classmethod:

```{autodoc2-docstring} unit_run.components.Unit._create_obj_by_raw_data
```

````

````{py:method} _check_before_save(save_path)
:canonical: unit_run.components.Unit._check_before_save

```{autodoc2-docstring} unit_run.components.Unit._check_before_save
```

````

````{py:method} _save(save_dir)
:canonical: unit_run.components.Unit._save

```{autodoc2-docstring} unit_run.components.Unit._save
```

````

````{py:method} set_param_group(name, group, with_check=True)
:canonical: unit_run.components.Unit.set_param_group

```{autodoc2-docstring} unit_run.components.Unit.set_param_group
```

````

````{py:method} set_param_group_from_disk(path, new_name=None)
:canonical: unit_run.components.Unit.set_param_group_from_disk

```{autodoc2-docstring} unit_run.components.Unit.set_param_group_from_disk
```

````

````{py:method} rename_param_group(old_name, new_name, overwrite=False)
:canonical: unit_run.components.Unit.rename_param_group

```{autodoc2-docstring} unit_run.components.Unit.rename_param_group
```

````

````{py:method} run(group_name)
:canonical: unit_run.components.Unit.run

```{autodoc2-docstring} unit_run.components.Unit.run
```

````

````{py:method} _get_param_group_map_dict()
:canonical: unit_run.components.Unit._get_param_group_map_dict

```{autodoc2-docstring} unit_run.components.Unit._get_param_group_map_dict
```

````

````{py:method} to_info_dict()
:canonical: unit_run.components.Unit.to_info_dict

```{autodoc2-docstring} unit_run.components.Unit.to_info_dict
```

````

````{py:property} src_obj_info
:canonical: unit_run.components.Unit.src_obj_info

```{autodoc2-docstring} unit_run.components.Unit.src_obj_info
```

````

````{py:method} __contains__(group_name)
:canonical: unit_run.components.Unit.__contains__

```{autodoc2-docstring} unit_run.components.Unit.__contains__
```

````

`````
