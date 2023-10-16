####
unit-run
####
*********
Description
*********
This package is used to simply run a unit *(only supports the ``Callable`` object currently)* in Python **without any extra running code**. And it can also save/load all your input parameters as/from a simple json file, so it is easy to run a target unit with auto-input parameters group by give it just a group name.

*********
Usage
*********
For example, if there is a file with two units (functions in this example):



Create a Unit from in-memory data
=======
```
unit_path = 'D:/documents/AcademicDocuments/customed_python_pkgs/unit-run/test.py'
unit_name = 'y'
unit = Unit(unit_path, unit_name)
print(unit)
```