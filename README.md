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

### 1. CLI Tool
For easy explaination in following usecases, we firstly suppose that we have created two parameter group json files manually:

-  tests/manual_p_group1.json
    ```json
    [10, 0]
    ```
-  tests/manual_p_group2.json
    ```json
    {"a": 100, "b": 99.5}
    ```

#### Perform a one-time unit running with a parameter group derived from a `json-str` or a `json` file
- Use `-g` or `--group` to pass `json-str`
    ```shell
    unit-run once tests/test.py y -g "[1, 2]"
    # run\cli.py once tests/test.py y -g "[1, 2]"
    # Running the target unit 'y' from tests/test.py...
    # Running complete, time consuming: 0.0 s.

    # **********Running Result**********
    # -1
    # **********Running Result**********
    ```

- Use `--file` to pass `json` file
    ```shell
    unit-run once tests/test.py y --file tests/manual_p_group1.json
    # Running the target unit 'y' from tests/test.py...
    # Running complete, time consuming: 0.0 s.

    # **********Running Result**********
    # 9
    # **********Running Result**********
    ```


#### Create a stored `Unit` for the following runs
```shell
unit-run create tests/test.py y tests/test -g name1 "[1,2]" name2 "{\"a\": 3, \"b\": 5}" --file-pairs name3 tests/manual_p_group1.json name4 tests/manual_p_group2.json

# The information of unit 'y' (from tests/test.py) saved at tests/test with 4 groups of paramters.
```

#### Inspect or view `Unit` information
- View an existing `Unit` by `--dir`
  - View the entire `Unit`
    ```shell
    unit-run view --dir tests/test

    #{
    #    "name": "y",
    #    "paramters": [
    #        {
    #          "name": "a",
    #          "annotation": "<class 'inspect._empty'>",
    #          "kind": "positional or keyword"
    #        },
    #        {
    #          "name": "b",
    #          "annotation": "<class 'inspect._empty'>",
    #          "kind": "positional or keyword"
    #        }
    #    ],
    #    "param_group_names": "['name1', 'name2', 'name3', 'name4']"
    #}
    ```
  - View the target parameter group of `Unit`
    ```shell
    unit-run view --dir tests/test name3

    # [10, 1]
    ```

- Inpect the target unit in a raw file by `--raw`
    ```shell
    unit-run view --raw tests/test.py y

    # {
    #   "name": "y",
    #   "paramters": [
    #     {
    #       "name": "a",
    #       "annotation": "<class 'inspect._empty'>",
    #       "kind": "positional or keyword"
    #     },
    #     {
    #       "name": "b",
    #       "annotation": "<class 'inspect._empty'>",
    #       "kind": "positional or keyword"
    #     }
    #   ]
    # }
    ```


#### Perform a running from a stored `Unit`
```shell
unit-run run tests/test name2

# Found 2 groups of paramters for 'y' unit in tests/test.py
# Running the target unit 'y' from tests/test.py...
# Running complete, time consuming: 0.0 s.

# **********Running Result**********
# -2
# **********Running Result**********
```

#### Set named parameter groups for a stored `Unit`
```shell
unit-run set tests/test -g name2 "[1, 1]" --file-pairs name4 tests/manual_p_group1.json name5 tests/manual_p_group2.json -f # Use '-f' or '-force-overwrite' to overwrite the existing parameter group.

# Found 4 groups of paramters for 'y' unit in tests/test.py
# Parameter group 'name2' overwrote.
# Parameter group 'name4' overwrote.
# New parameter group 'name5' added.
```

#### Delete named parameter groups or entire `Unit` for a stored `Unit`
- Delete parameter groups by names
    ```shell
    unit-run del tests/test name4 name5

    # Deleted 2 parameter groups of the unit 'y'.
    ```

- Clear all parameter groups of a `Unit`
    ```shell
    unit-run del tests/test *

    # The parameters groups of unit 'y' cleared.
    ```

- Delete the entire `Unit`
    ```shell
    unit-run del tests/test

    # The entire unit 'y' was deleted.
    ```


#### You can always set the `-q` or `--quiet` flag to mute the log
```shell
unit-run -q once tests/test.py y "[1, 2]"
unit-run --quiet create tests/test.py y tests/test -p name1 "[1,2]" name2 "{\"a\": 3, \"b\": 5}" 
unit-run -q run tests/test name2
...
```

### 2. Python Script
#### Create a `Unit` object from scratch in memory
``` python
unit = Unit(unit_path, unit_name)

# use positional parameters
unit.set_param_group('test1', [8, 10])
# use keyword parameters
unit.set_param_group('test2', {'a': 100, 'b': 99})
```

#### Perform a unit running by parameter group name
```python
unit.run('test1') # -2
unit.run('test2') # 1
```

#### Save the `Unit` object with all parameter groups
```python
# Notice: The save path need to be a directory (not necessarily exist)
save_dir = './test'
unit.save(save_dir, verbose=True)
```
>Remember that, you can always to directly modify the *{group_name}.param_group.json* in `save_dir` to change your parameter setting or even create a new parameter group by manually create a json file.

#### Load the `Unit` object with the paramter groups from disk
```python
# Notice: Again, the save path need to be a directory (not necessarily exist)
load_dir = './test'
unit = Unit.load_from_dir(load_dir, verbose=True)
```

#### Get the `dict-like` summary for `Unit` object
```python
summary = unit.summary
```


## To do
- Support for any code segment and the classes from popular package like `numpy.ndarray`.
- Support for complete storage for `Unit` (including the target unit object).
- Maybe create a new buldled file extension named `.unit` to pack all the data files into a single file and provide graphic user interface to get access to it.
- Support for multiple languages.