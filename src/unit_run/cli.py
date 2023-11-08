import argparse, json, shutil
from time import perf_counter
import os, sys
sys.path.append(os.path.abspath(os.path.join(__file__, '')))
from components import Unit
from utils import load_json

def set_file_pairs(unit, pairs, force_overwrite, quiet):
    assert len(pairs)%2 == 0
    for i in range(len(pairs)//2):
        path = pairs[i*2+1]
        with open(path) as f:
            pairs[i*2+1] = f.read()
    set_parameter_pairs(unit, pairs, force_overwrite, quiet)

def set_parameter_pairs(unit, pairs, force_overwrite, quiet):
    assert len(pairs)%2 == 0
    for i in range(len(pairs)//2):
        k, param_group = pairs[i*2], json.loads(pairs[i*2+1])
        if not force_overwrite and k in unit:
            raise NameError(f"The parameter group '{k}' has already existed, please use '-F' or '--force-overwrite' to overwrite.")
        else:
            if not quiet:
                if force_overwrite and k in unit:
                    print(f"Parameter group '{k}' overwrote.")
                else:
                    print(f"New parameter group '{k}' added.")
            unit.set_param_group(k, param_group)

def run(unit, pname, quiet=False):
    name, path = unit.src_name, unit.src_path
    if not quiet:
        print(f"Running the target unit '{name}' from {path}...")
        start_t = perf_counter()
        result = unit.run(pname)
        print(f'Running complete, time consuming: {round(perf_counter()-start_t, 2)} s.\n')
        print('*'*10 + 'Running Result' + '*'*10)
        print(result)
        print('*'*10 + 'Running Result' + '*'*10)
    else:
        result = unit.run(pname)

def build_sub_once_parser(parsers):
    parser = parsers.add_parser('once', help='Perform a unit running without any information storage.')
    parser.add_argument('upath', help='The file path where the unit is located.')
    parser.add_argument('uname', help='The name of the target unit.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-j', '--json-str', help='The JSON str that will be parsed as a parameter group for the target unit.')
    group.add_argument('-f', '--file', help='The path of JSON file whose content will be parsed as a parameter group for the target unit.')

    def func(args):
        unit = Unit(args.upath, args.uname)
        group = json.loads(args.json_str) if args.json_str is not None else load_json(args.file)
        unit.set_param_group('Unnamed', group)
        run(unit, 'Unnamed', args.quiet)


    parser.set_defaults(func=func)

def build_sub_create_parser(parsers):
    parser = parsers.add_parser('create', help='Create Unit object with storage.')
    parser.add_argument('upath', help='The file path where the unit is located.')
    parser.add_argument('uname', help='The name of the target unit.')
    parser.add_argument('save_dir', help="The directory to save the unit infomation.")
    parser.add_argument('-j', '--json-str-pairs', 
                                   nargs='+',
                                   help='Key-value parameters groups to initiate the unit. \nExample: -g name1 "[1, 2]" name2 "{\'a\': 1, \'b\': 2}"')
    parser.add_argument('-f', '--file-pairs', 
                                   nargs='+',
                                   help='Key-json_path parameters groups to initiate the unit. \nExample: --file-pairs tests/name1 manual_p_group1.json name2 tests/manual_p_group2.json')

    def func(args):
        # print(args)
        unit = Unit(args.upath, args.uname)
        if args.json_str_pairs is not None:
            set_parameter_pairs(unit, args.json_str_pairs, True, True)
        if args.file_pairs is not None:
            set_file_pairs(unit, args.file_pairs, True, True)
        unit.save_to_disk(args.save_dir)
        # print(args.save_dir)

    parser.set_defaults(func=func)

def build_sub_run_parser(parsers):
    parser = parsers.add_parser('run', help='Perform a running from a stored Unit.')
    parser.add_argument('load_dir', help="The directory to load the unit infomation.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', '--group-name', help="The name of parameter group.")
    group.add_argument('-j', '--json-str', help="Json-string-like parameters to perform a unit run.")
    group.add_argument('-f', '--file', help="Json file whose content will be transformed into parameters to perform a unit run.")
    def func(args):
        # print(args)
        unit = Unit.load_from_disk(args.load_dir)
        if args.group_name is not None:
            group_name = args.group_name
        else:
            group_name = 'Unnamed'
            group = json.loads(args.json_str) if args.json_str is not None else load_json(args.file)
            unit.set_param_group(group_name, group)
        run(unit, group_name, args.quiet)

    parser.set_defaults(func=func)

def build_sub_view_parser(parsers):
    parser = parsers.add_parser('view', help='List information about the target unit.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--dir', nargs='+', help="Unit directory path to print information.")
    group.add_argument('--raw', nargs='+', help="Print information by a raw unit file.")

    
    def func(args):
        if args.dir is not None:
            unit = Unit.load_from_disk(args.dir[0])
            if len(args.dir) == 1:
                summary = unit.to_info_dict()
                info = summary['meta']
                info['param_group_names'] = str(list(summary['param_group_map'].keys()))
                print(json.dumps(info, indent=2))
            else:
                group_name = args.dir[1]
                print(unit.param_group_map[group_name])
        else:
            unit = Unit(args.raw[0], args.raw[1])
            print(json.dumps(unit.src_obj_info, indent=2))
        # set_parameter_pairs(unit, args.json_str_pairs, args.force_overwrite, args.quiet)
        # set_file_pairs(unit, args.file_pairs, args.force_overwrite, args.quiet)
        # unit.save(args.load_dir, verbose=False)
        
    parser.set_defaults(func=func)

def build_sub_set_parser(parsers):
    parser = parsers.add_parser('set', help='Set named parameter groups for a stored Unit.')
    parser.add_argument('load_dir', help="The directory to load the unit infomation.")
    parser.add_argument('-F', '--force-overwrite', action='store_true', help='Whether to overwrite existing parameter group.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--rename', nargs='+', help="(old_name, new_name) Set a new parameter group from a old group.")
    group.add_argument('-j', '--json-str-pairs', nargs='+', help='Key-value parameters groups to initiate the unit. \nExample: -g name1 "[1, 2]" name2 "{\'a\': 1, \'b\': 2}"')
    group.add_argument('-f', '--file-pairs', 
                                   nargs='+',
                                   help='Key-json_path parameters groups to initiate the unit. \nExample: --file-pairs tests/name1 manual_p_group1.json name2 tests/manual_p_group2.json')
    
    def func(args):
        # print(args)
        unit = Unit.load_from_disk(args.load_dir)
        if args.rename is not None:
            if len(args.rename) != 2:
                raise ValueError(f'The number of names to rename should be 2 (old name and new name), not {len(args.rename)}.')
            else:
                old_name, new_name = args.rename
                unit.rename_param_group(old_name, new_name, args.force_overwrite)
        elif args.json_str_pairs is not None:
            if len(args.json_str_pairs) % 2 != 0:
                raise ValueError(f'The number of pairs should be even, not odd: {len(args.json_str_pairs)}.')
            set_parameter_pairs(unit, args.json_str_pairs, args.force_overwrite, args.quiet)
        elif args.file_pairs is not None:
            if len(args.file_pairs) % 2 != 0:
                raise ValueError(f'The number of pairs should be even, not odd: {len(args.file_pairs)}.')
            set_file_pairs(unit, args.file_pairs, args.force_overwrite, args.quiet)
        unit.save_to_disk(args.load_dir)
        if not args.quiet:
            print('Parameter group set completely.')
        
    parser.set_defaults(func=func)

def build_sub_del_parser(parsers):
    parser = parsers.add_parser('del', help='Delete named parameter groups or entire Unit for a stored Unit.')
    parser.add_argument('load_dir', help="The directory to load the unit infomation, delete the entire Unit direcotry when group_names is empty.")
    parser.add_argument('group_names', default=[], nargs='*', help='The names of parameter groups to be deleted. Example: del tests/test name1 name2 name3')
    
    def func(args):
        group_names = args.group_names
        unit = Unit.load_from_disk(args.load_dir)
        if len(group_names) == 0:
            shutil.rmtree(args.load_dir)
            if not args.quiet:
                print(f"The entire unit '{unit.src_name}' was deleted.")
        elif len(group_names) == 1 and group_names[0] == '*':
            unit.param_group_map = dict()
            unit.save_to_disk(args.load_dir)
            if not args.quiet:
                print(f"The parameters groups of unit '{unit.src_name}' cleared.")
        else:
            for name in group_names:
                del unit.param_group_map[name]
            unit.save_to_disk(args.load_dir)
            if not args.quiet:
                print(f"Deleted {len(group_names)} parameter group{'s' if len(group_names) > 1 else ''} of the unit '{unit.src_name}'.")
        # unit = Unit.load_from_disk(args.load_dir, verbose=not args.quiet)
        # set_parameter_pairs(unit, args.json_str_pairs, args.force_overwrite, args.quiet)
        # set_file_pairs(unit, args.file_pairs, args.force_overwrite, args.quiet)
        # unit.save(args.load_dir, verbose=False)
        
    parser.set_defaults(func=func)

def main():
    parser = argparse.ArgumentParser(description='CLI for simple unit running.', prog='unit_run')
    parser.add_argument('-q', '--quiet', action='store_true', help='Whether to hide the log during running (including reuslt print).')
    

    sub_parsers = parser.add_subparsers(title='subcommands')
    build_sub_once_parser(sub_parsers)
    build_sub_create_parser(sub_parsers)
    build_sub_run_parser(sub_parsers)
    build_sub_view_parser(sub_parsers)
    build_sub_set_parser(sub_parsers)
    build_sub_del_parser(sub_parsers)

    args = parser.parse_args()
    args.func(args)

    

if __name__ == '__main__':
    main()