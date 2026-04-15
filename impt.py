import os
from eval_code import eval_code
from variables import variables
from fun import fun_list

_imported_files = set()
_imported_files_data = {}

def impt(filename):
    filename = filename.strip()
    if not filename.endswith(".k"):
        filename += ".k"
    if filename in _imported_files:
        return
    if not os.path.exists(filename):
        print(f"\033[33m::\033[31mError\033[33m:: \033[32mfile '\033[33m{filename}\033[32m' not found !")
        return
    file_vars = set()
    file_funcs = []
    try:
        with open(filename, "r") as f:
            lines = f.read().splitlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            pre_vars = set(variables.keys())
            pre_funcs = list(fun_list)
            eval_code(line)
            new_vars = set(variables.keys()) - pre_vars
            file_vars.update(new_vars)
            new_funcs = [f for f in fun_list if f not in pre_funcs]
            file_funcs.extend(new_funcs)
        _imported_files.add(filename)
        _imported_files_data[filename] = {"variables": file_vars, "functions": file_funcs}
    except Exception as e:
        print(f"\033[33m::\033[31mError\033[33m:: \033[35mError while importing '{filename}': {e}")
