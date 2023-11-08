import inspect, sys, os, importlib, json
from enum import Enum
import functools

def inspect_by_path(path: str, filter_func=None, with_name=False):
    """
     Inspect a module and return a list of objects that passed a test by the filter funciton. 
     
     :param path: The path to inspect.
     :param filter_func: A function that takes a module member as parameter and returns whether one member should be included in the results.
     :param with_name: If True the name of the object will be included in the result.
     :returns: A list of ( name object ) tuples. If no path is given an empty list is returned. >>> from machinery
    """
    # Return an array of paths to the file or an empty list if the path does not exist.
    if not os.path.exists(path):
        return []
    sys.path.append(os.path.dirname(path))
    filter_func = filter_func if filter_func is not None else ((lambda obj: True) if not with_name else (lambda obj, name: True))
    _tmp_module = importlib.machinery.SourceFileLoader('_tmp_module', path).load_module()
    results = []
    # Return a list of all the objects in the module.
    for name, obj in inspect.getmembers(_tmp_module):
        param = [obj, name] if with_name else [obj]
        # Add a new object to the results list.
        if filter_func(*param):
            results.append((name, obj) if with_name else obj)
    return results
    

def inspect_callables_by_path(path):
    """
     Inspect a file and return a list of callables. This is a wrapper around inspect_by_path with the exception that we don't want to inspect classes or functions that are in _tmp_module.
     
     :param path: Path to the file to inspect. Can be a file or a directory.
     :returns: A list of inspect. Classes or inspect. Function objects in the file at the given path. If there are no calls to the file it returns an empty list
    """
    def filter_func(obj):
        """
         Filter function to determine if it is a class or function. This is used to prevent __init__ from being called for classes that inherit from _tmp_module
         
         :param obj: The object to inspect.
         :returns: True if the object is a class or function False otherwise. >>> filter_func ( lambda obj : obj. __class__ =='__init__ '
        """
        return (inspect.isclass(obj) or inspect.isfunction(obj)) and obj.__module__ == '_tmp_module'
    return inspect_by_path(path, filter_func, with_name=False)

def get_info_dict_from_callable(c):
    """
     Get information about a callable. This is used to generate a JSON - serializable dictionary that can be serialized to JSON.
     
     :param c: The callable to get information about. Must be a callable
     :returns: A dictionary containing information about the
    """
    info = {
        'name': c.__name__,
        'paramters': []
    }
    # Add parameters to the info paramters.
    for p in inspect.signature(c).parameters.values():
        item = {
            'name': p.name,
            'annotation': str(p.annotation),
            'kind': p.kind.description
        }
        # Set default value of item
        if p.default is not p.empty:
            item['default'] = p.default
        info['paramters'].append(item)
    return info

def inspect_callable_infos_by_path(path):
    """
     Inspects callable infos by path. This is a wrapper around inspect_callables_by_path that returns a list of dictionaries.
     
     :param path: Path to inspect callable infos. Can be a file path or a string containing globs.
     :returns: A list of dictionaries one for each callable that has been inspected. Each dictionary is a dictionary with keys corresponding to the callable's name and values corresponding to the information returned by get_info_dict_from_callable
    """
    result_infos = []
    # Returns a list of all callable functions in the callables by path.
    for c in inspect_callables_by_path(path):
        result_infos.append(get_info_dict_from_callable(c))
    return result_infos
    # callable_sigs = [inspect.signature(c) for c in ] 
    # callable_infos = [{

    # } for sig in callable_sigs]
def find_callable_by_name(path, name):
    """
     Find callable by name. This is a wrapper around inspect_callables_by_path to search for callable with given name.
     
     :param path: Path to the callable in Celery.
     :param name: Name of callable to find. It must be a string.
     :returns: Callable if found None otherwise. >>> from sympy. utilities. iterables import find_callable_by_name Traceback ( most recent call last ) : TypeError : name is
    """
    result = list(filter(lambda c: c.__name__ == name, inspect_callables_by_path(path)))
    return result[0] if len(result) > 0 else None

def load_json(json_path):
    """
     Load a JSON file from the given path.
     
     :param json_path: Path to the JSON file. Must be a string.
     :returns: An object of the JSON file that was loaded from the file at ` json_path `. See : func : ` json. load ` for details
    """
    with open(str(json_path)) as f:
        return json.load(f)
    
def save_as_json(json_path, obj, indent=2):
    """
     Saves a python object as JSON. This is a convenience function for creating a file in the same directory as the json_path
     
     :param json_path: Path to the JSON file
     :param obj: Object to be saved as JSON. It can be any python object
     :param indent: Number of spaces to indent JSON output default is
    """
    with open(str(json_path), 'w') as f:
        json.dump(obj, f, indent=indent)

class PathType(Enum):
    FILE = 1
    DIRECTORY = 2
    BOTH = 3


def auto_type_check(func):
    """
     Decorator to check type of parameters. This decorator is used to check the type of parameters passed to a function by inspecting the function signature.
     
     :param func: function to be wrapped. It must have at least one parameter
     :returns: wrapped function with type
    """
    @functools.wraps(func)
    def wrap(*param, **kwargs):
        """
         Wrap function with annotations. This is a wrapper for func ( * param ** kwargs ). The arguments are passed to func as positional arguments and the keyword arguments are passed as keyword arguments.
         
         :returns: result of func ( * param ** kwargs ) with annotations applied to the parameter values if annotations are present
        """
        # Check if the argument is a parameter type.
        for i, (k, p) in enumerate(inspect.signature(func).parameters.items()):
            t = p.annotation
            # TypeError if argument is not of type t.
            if t != inspect._empty:
                arg_value = param[i] if len(param) > i else kwargs[k]
                # TypeError if argument_value is not of type t.
                if not isinstance(arg_value, t):
                    raise TypeError(f"Argument '{k}' should be '{t}' type, not '{type(arg_value)}' type.")
        return func(*param, **kwargs)    
    return wrap

def _test(a):
    """
     This is a test function. It should be used in a unit test as the first argument to the function
     
     :param a: The object to test
    """
    pass