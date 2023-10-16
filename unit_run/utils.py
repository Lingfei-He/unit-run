import inspect, sys, os, importlib

def inspect_callables_by_path(path):
    callables = []
    sys.path.append(os.path.dirname(path))
    _tmp_model = importlib.machinery.SourceFileLoader('_tmp_model', path).load_module()
    for name, obj in inspect.getmembers(_tmp_model):
        if (inspect.isclass(obj) or inspect.isfunction(obj)) and obj.__module__ == '_tmp_model':
            callables.append(obj)
    return callables

def get_info_dict_from_callable(c):
    info = {
        'name': c.__name__,
        'paramters': []
    }
    for p in inspect.signature(c).parameters.values():
        item = {
            'name': p.name,
            'annotation': str(p.annotation),
            'kind': p.kind.description
        }
        if p.default is not p.empty:
            item['default'] = p.default
        info['paramters'].append(item)
    return info

def inspect_callable_infos_by_path(path):
    result_infos = []
    for c in inspect_callables_by_path(path):
        result_infos.append(get_info_dict_from_callable(c))
    return result_infos
    # callable_sigs = [inspect.signature(c) for c in ] 
    # callable_infos = [{

    # } for sig in callable_sigs]
def find_callable_by_name(path, name):
    result = list(filter(lambda c: c.__name__ == name, inspect_callables_by_path(path)))
    return result[0] if len(result) > 0 else None