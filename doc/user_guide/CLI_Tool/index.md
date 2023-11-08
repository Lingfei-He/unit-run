# CLI Tool
For easy explaination in following usecases, we firstly suppose that we have created two parameter group json files manually:

<!-- `````{admonition} Example -->
````{list-table}
* - ```{code-block} python
        :caption: test.py
    def x(a, b):
        return a+b

    def y(a, b):
        return a-b
    ```
  - ```{code-block} json
        :caption: manual_p_group1.json
    [
        10, 0
    ]
    ```
  - ```{code-block} json
    :caption: manual_p_group2.json
    [
        10, 0
    ]
    ```
````
<!-- ````` -->

## You can always set the `-q` or `--quiet` flag to mute the log
```shell
unit-run -q once tests/test.py y "[1, 2]"
unit-run --quiet create tests/test.py y tests/test -j name1 "[1,2]" name2 "{\"a\": 3, \"b\": 5}" 
unit-run -q run tests/test -g name2
...
```