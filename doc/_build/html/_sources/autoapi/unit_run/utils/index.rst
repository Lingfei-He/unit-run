:py:mod:`unit_run.utils`
========================

.. py:module:: unit_run.utils


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   unit_run.utils.PathType



Functions
~~~~~~~~~

.. autoapisummary::

   unit_run.utils.inspect_by_path
   unit_run.utils.inspect_callables_by_path
   unit_run.utils.get_info_dict_from_callable
   unit_run.utils.inspect_callable_infos_by_path
   unit_run.utils.find_callable_by_name
   unit_run.utils.load_json
   unit_run.utils.save_as_json
   unit_run.utils.auto_type_check
   unit_run.utils._test



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


