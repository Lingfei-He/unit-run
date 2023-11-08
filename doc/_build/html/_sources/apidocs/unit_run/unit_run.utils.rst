:py:mod:`unit_run.utils`
========================

.. py:module:: unit_run.utils

.. autodoc2-docstring:: unit_run.utils
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PathType <unit_run.utils.PathType>`
     -

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`inspect_by_path <unit_run.utils.inspect_by_path>`
     - .. autodoc2-docstring:: unit_run.utils.inspect_by_path
          :summary:
   * - :py:obj:`inspect_callables_by_path <unit_run.utils.inspect_callables_by_path>`
     - .. autodoc2-docstring:: unit_run.utils.inspect_callables_by_path
          :summary:
   * - :py:obj:`get_info_dict_from_callable <unit_run.utils.get_info_dict_from_callable>`
     - .. autodoc2-docstring:: unit_run.utils.get_info_dict_from_callable
          :summary:
   * - :py:obj:`inspect_callable_infos_by_path <unit_run.utils.inspect_callable_infos_by_path>`
     - .. autodoc2-docstring:: unit_run.utils.inspect_callable_infos_by_path
          :summary:
   * - :py:obj:`find_callable_by_name <unit_run.utils.find_callable_by_name>`
     - .. autodoc2-docstring:: unit_run.utils.find_callable_by_name
          :summary:
   * - :py:obj:`load_json <unit_run.utils.load_json>`
     - .. autodoc2-docstring:: unit_run.utils.load_json
          :summary:
   * - :py:obj:`save_as_json <unit_run.utils.save_as_json>`
     - .. autodoc2-docstring:: unit_run.utils.save_as_json
          :summary:
   * - :py:obj:`auto_type_check <unit_run.utils.auto_type_check>`
     - .. autodoc2-docstring:: unit_run.utils.auto_type_check
          :summary:
   * - :py:obj:`_test <unit_run.utils._test>`
     - .. autodoc2-docstring:: unit_run.utils._test
          :summary:

API
~~~

.. py:function:: inspect_by_path(path: str, filter_func=None, with_name=False)
   :canonical: unit_run.utils.inspect_by_path

   .. autodoc2-docstring:: unit_run.utils.inspect_by_path

.. py:function:: inspect_callables_by_path(path)
   :canonical: unit_run.utils.inspect_callables_by_path

   .. autodoc2-docstring:: unit_run.utils.inspect_callables_by_path

.. py:function:: get_info_dict_from_callable(c)
   :canonical: unit_run.utils.get_info_dict_from_callable

   .. autodoc2-docstring:: unit_run.utils.get_info_dict_from_callable

.. py:function:: inspect_callable_infos_by_path(path)
   :canonical: unit_run.utils.inspect_callable_infos_by_path

   .. autodoc2-docstring:: unit_run.utils.inspect_callable_infos_by_path

.. py:function:: find_callable_by_name(path, name)
   :canonical: unit_run.utils.find_callable_by_name

   .. autodoc2-docstring:: unit_run.utils.find_callable_by_name

.. py:function:: load_json(json_path)
   :canonical: unit_run.utils.load_json

   .. autodoc2-docstring:: unit_run.utils.load_json

.. py:function:: save_as_json(json_path, obj, indent=2)
   :canonical: unit_run.utils.save_as_json

   .. autodoc2-docstring:: unit_run.utils.save_as_json

.. py:class:: PathType
   :canonical: unit_run.utils.PathType

   Bases: :py:obj:`enum.Enum`

   .. py:attribute:: FILE
      :canonical: unit_run.utils.PathType.FILE
      :value: 1

      .. autodoc2-docstring:: unit_run.utils.PathType.FILE

   .. py:attribute:: DIRECTORY
      :canonical: unit_run.utils.PathType.DIRECTORY
      :value: 2

      .. autodoc2-docstring:: unit_run.utils.PathType.DIRECTORY

   .. py:attribute:: BOTH
      :canonical: unit_run.utils.PathType.BOTH
      :value: 3

      .. autodoc2-docstring:: unit_run.utils.PathType.BOTH

.. py:function:: auto_type_check(func)
   :canonical: unit_run.utils.auto_type_check

   .. autodoc2-docstring:: unit_run.utils.auto_type_check

.. py:function:: _test(a)
   :canonical: unit_run.utils._test

   .. autodoc2-docstring:: unit_run.utils._test
