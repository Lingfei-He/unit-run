:py:mod:`unit_run`
==================

.. py:module:: unit_run


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cli/index.rst
   components/index.rst
   utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   unit_run.PathType
   unit_run.PathType
   unit_run.Base
   unit_run.Meta
   unit_run.ParameterGroup
   unit_run.Unit



Functions
~~~~~~~~~

.. autoapisummary::

   unit_run.inspect_by_path
   unit_run.inspect_callables_by_path
   unit_run.get_info_dict_from_callable
   unit_run.inspect_callable_infos_by_path
   unit_run.find_callable_by_name
   unit_run.load_json
   unit_run.save_as_json
   unit_run.auto_type_check
   unit_run._test
   unit_run.save_as_json
   unit_run.load_json
   unit_run.auto_type_check
   unit_run.get_info_dict_from_callable
   unit_run.find_callable_by_name



.. py:function:: inspect_by_path(path: str, filter_func=None, with_name=False)

   Inspect a module and return a list of objects that passed a test by the filter funciton.

   :param path: The path to inspect.
   :param filter_func: A function that takes a module member as parameter and returns whether one member should be included in the results.
   :param with_name: If True the name of the object will be included in the result.
   :returns: A list of ( name object ) tuples. If no path is given an empty list is returned. >>> from machinery


.. py:function:: inspect_callables_by_path(path)

   Inspect a file and return a list of callables. This is a wrapper around inspect_by_path with the exception that we don't want to inspect classes or functions that are in _tmp_module.

   :param path: Path to the file to inspect. Can be a file or a directory.
   :returns: A list of inspect. Classes or inspect. Function objects in the file at the given path. If there are no calls to the file it returns an empty list


.. py:function:: get_info_dict_from_callable(c)

   Get information about a callable. This is used to generate a JSON - serializable dictionary that can be serialized to JSON.

   :param c: The callable to get information about. Must be a callable
   :returns: A dictionary containing information about the


.. py:function:: inspect_callable_infos_by_path(path)

   Inspects callable infos by path. This is a wrapper around inspect_callables_by_path that returns a list of dictionaries.

   :param path: Path to inspect callable infos. Can be a file path or a string containing globs.
   :returns: A list of dictionaries one for each callable that has been inspected. Each dictionary is a dictionary with keys corresponding to the callable's name and values corresponding to the information returned by get_info_dict_from_callable


.. py:function:: find_callable_by_name(path, name)

   Find callable by name. This is a wrapper around inspect_callables_by_path to search for callable with given name.

   :param path: Path to the callable in Celery.
   :param name: Name of callable to find. It must be a string.
   :returns: Callable if found None otherwise. >>> from sympy. utilities. iterables import find_callable_by_name Traceback ( most recent call last ) : TypeError : name is


.. py:function:: load_json(json_path)

   Load a JSON file from the given path.

   :param json_path: Path to the JSON file. Must be a string.
   :returns: An object of the JSON file that was loaded from the file at ` json_path `. See : func : ` json. load ` for details


.. py:function:: save_as_json(json_path, obj, indent=2)

   Saves a python object as JSON. This is a convenience function for creating a file in the same directory as the json_path

   :param json_path: Path to the JSON file
   :param obj: Object to be saved as JSON. It can be any python object
   :param indent: Number of spaces to indent JSON output default is


.. py:class:: PathType


   Bases: :py:obj:`enum.Enum`

   Generic enumeration.

   Derive from this class to define new enumerations.

   .. py:attribute:: FILE
      :value: 1

      

   .. py:attribute:: DIRECTORY
      :value: 2

      

   .. py:attribute:: BOTH
      :value: 3

      


.. py:function:: auto_type_check(func)

   Decorator to check type of parameters. This decorator is used to check the type of parameters passed to a function by inspecting the function signature.

   :param func: function to be wrapped. It must have at least one parameter
   :returns: wrapped function with type


.. py:function:: _test(a)

   This is a test function. It should be used in a unit test as the first argument to the function

   :param a: The object to test


.. py:class:: PathType


   Bases: :py:obj:`enum.Enum`

   Generic enumeration.

   Derive from this class to define new enumerations.

   .. py:attribute:: FILE
      :value: 1

      

   .. py:attribute:: DIRECTORY
      :value: 2

      

   .. py:attribute:: BOTH
      :value: 3

      


.. py:function:: save_as_json(json_path, obj, indent=2)

   Saves a python object as JSON. This is a convenience function for creating a file in the same directory as the json_path

   :param json_path: Path to the JSON file
   :param obj: Object to be saved as JSON. It can be any python object
   :param indent: Number of spaces to indent JSON output default is


.. py:function:: load_json(json_path)

   Load a JSON file from the given path.

   :param json_path: Path to the JSON file. Must be a string.
   :returns: An object of the JSON file that was loaded from the file at ` json_path `. See : func : ` json. load ` for details


.. py:function:: auto_type_check(func)

   Decorator to check type of parameters. This decorator is used to check the type of parameters passed to a function by inspecting the function signature.

   :param func: function to be wrapped. It must have at least one parameter
   :returns: wrapped function with type


.. py:function:: get_info_dict_from_callable(c)

   Get information about a callable. This is used to generate a JSON - serializable dictionary that can be serialized to JSON.

   :param c: The callable to get information about. Must be a callable
   :returns: A dictionary containing information about the


.. py:function:: find_callable_by_name(path, name)

   Find callable by name. This is a wrapper around inspect_callables_by_path to search for callable with given name.

   :param path: Path to the callable in Celery.
   :param name: Name of callable to find. It must be a string.
   :returns: Callable if found None otherwise. >>> from sympy. utilities. iterables import find_callable_by_name Traceback ( most recent call last ) : TypeError : name is


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



