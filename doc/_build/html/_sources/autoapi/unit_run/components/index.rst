:py:mod:`unit_run.components`
=============================

.. py:module:: unit_run.components


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   unit_run.components.Base
   unit_run.components.Meta
   unit_run.components.ParameterGroup
   unit_run.components.Unit




.. py:class:: Base


   Bases: :py:obj:`abc.ABC`

   Helper class that provides a standard way to create an ABC using
   inheritance.

   .. py:property:: valid


   .. py:attribute:: PATH_TYPE

      

   .. py:method:: check_data(data)
      :classmethod:


   .. py:method:: validate_data(*args, **kwargs)


   .. py:method:: check()


   .. py:method:: _check_file_name(file_name)
      :classmethod:


   .. py:method:: _check_path_to_load(load_path)
      :classmethod:


   .. py:method:: _check_before_load(load_path)
      :classmethod:


   .. py:method:: _load_raw_data(load_path)
      :classmethod:


   .. py:method:: _check_after_load(raw_data)
      :classmethod:


   .. py:method:: is_path_loadable(load_path)
      :classmethod:


   .. py:method:: _create_obj_by_raw_data(raw_data)
      :classmethod:


   .. py:method:: _update(other_obj)


   .. py:method:: load_from_disk(load_path)
      :classmethod:


   .. py:method:: valid_path_exists(path)
      :classmethod:


   .. py:method:: _check_before_save(save_path)


   .. py:method:: _save(save_path)
      :abstractmethod:


   .. py:method:: _after_save(save_path)


   .. py:method:: _exist_handler(path)
      :classmethod:


   .. py:method:: save_to_disk(save_path, all_overwrite=True)


   .. py:method:: to_dict()


   .. py:method:: to_info_dict()


   .. py:method:: __str__() -> str

      Return str(self).



.. py:class:: Meta(src_path: str, src_name: str)


   Bases: :py:obj:`Base`

   Helper class that provides a standard way to create an ABC using
   inheritance.

   .. py:attribute:: FILE_NAME
      :value: '.meta.json'

      

   .. py:attribute:: PATH_TYPE

      

   .. py:method:: check_data(*param, **kwargs)
      :classmethod:


   .. py:method:: get_path_by_dir(meta_dir)
      :classmethod:


   .. py:method:: property(func)
      :classmethod:


   .. py:method:: _check_file_name(file_name)
      :classmethod:


   .. py:method:: _load_raw_data(load_path)
      :classmethod:


   .. py:method:: _check_after_load(raw_data)
      :classmethod:


   .. py:method:: _create_obj_by_raw_data(raw_data)
      :classmethod:


   .. py:method:: _save(save_path)



.. py:class:: ParameterGroup(data)


   Bases: :py:obj:`Base`

   Helper class that provides a standard way to create an ABC using
   inheritance.

   .. py:attribute:: FILE_SUFFIX
      :value: '.param_group.json'

      

   .. py:attribute:: PATH_TYPE

      

   .. py:method:: check_data(data)
      :classmethod:


   .. py:method:: check()


   .. py:method:: get_file_name(name)
      :classmethod:


   .. py:method:: get_path_by_dir_and_name(dir_path, name)
      :classmethod:


   .. py:method:: get_name_from_path(path)
      :classmethod:


   .. py:method:: _check_file_name(file_name)
      :classmethod:


   .. py:method:: _load_raw_data(load_path)
      :classmethod:


   .. py:method:: load_by_dir_and_name(dir_path, name)
      :classmethod:


   .. py:method:: _save(save_path)


   .. py:method:: save_by_dir_and_name(dir_path, name)



.. py:class:: Unit(src_path, src_name)


   Bases: :py:obj:`Base`

   Helper class that provides a standard way to create an ABC using
   inheritance.

   .. py:property:: src_obj_valid


   .. py:property:: src_obj


   .. py:property:: unit_info


   .. py:property:: summary


   .. py:attribute:: PATH_TYPE

      

   .. py:method:: src_path()


   .. py:method:: src_name()


   .. py:method:: check_data(unit)
      :classmethod:


   .. py:method:: check_src_obj()


   .. py:method:: _check_path_to_load(load_path)
      :classmethod:


   .. py:method:: _check_after_load(raw_data)
      :classmethod:


   .. py:method:: _load_raw_data(load_dir)
      :classmethod:


   .. py:method:: _create_obj_by_raw_data(raw_data)
      :classmethod:


   .. py:method:: _check_before_save(save_path)


   .. py:method:: _save(save_dir)


   .. py:method:: set_param_group(name, group, with_check=True)


   .. py:method:: run(group_name)


   .. py:method:: to_info_dict()


   .. py:method:: __contains__(group_name)



