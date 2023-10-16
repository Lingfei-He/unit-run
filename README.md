# unit-run
## Description

This package is used to simply run a unit *(only supports the ``Callable`` object currently)* in Python **without any extra running code**. And it can also save/load all your input parameters as/from a simple json file, so it is easy to run a target unit with auto-input parameters group by give it just a group name.
## Installation
```
pip install unit-run
```
## Usage
For example, we suppose that there is a file `test.py` with two units (functions in this example):
``` python
# ./test.py
def x(a, b):
    return a+b

def y(a, b):
    return a-b
```
And we also suppose that the target unit we want to run is the function `y(a, b)`.
```python
unit_path = './test.py'
unit_name = 'y'
```

### Create a `Unit` object from scratch in memory
``` python
unit = Unit(unit_path, unit_name)

# use positional parameters
unit.set_param_group('test1', [8, 10])
# use keyword parameters
unit.set_param_group('test2', {'a': 100, 'b': 99})
```

### Perform a unit running by parameter group name
```python
unit.run('test1') # -2
unit.run('test2') # 1
```

### Save the `Unit` object with all parameter groups
```python
# Notice: The save path need to be a directory (not necessarily exist)
save_dir = './test'
unit.save(save_dir, verbose=True)
```
>Remember that, you can always to directly modify the *{group_name}.param_group.json* in `save_dir` to change your parameter setting or even create a new parameter group by manually create a json file.

### Load the `Unit` object with the paramter groups from disk
```python
# Notice: Again, the save path need to be a directory (not necessarily exist)
load_dir = './test'
unit = Unit.load_from_dir(load_dir, verbose=True)
```

### Get the `dict-like` summary for `Unit` object
```python
summary = unit.summary
```


## To do
- Support for any code segment and the classes from popular package like `numpy.ndarry`.
- Support for complete storage for `Unit` (including the target unit object).
- Maybe create a new buldled file extension named `.unit` to pack all the data files into a single file and provide graphic user interface to get access to it.
- Support for multiple languages.