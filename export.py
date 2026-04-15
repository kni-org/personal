from variables import variables
from fun import fun_list
from impt import _imported_files, _imported_files_data

def expt(module_name):
    module_name = module_name.strip()
    if not module_name.endswith(".k"):
        module_name += ".k"
    if module_name not in _imported_files:
        print(f"\033[33m::\033[31mError\033[33m:: \033[35mModule '{module_name}' not imported!")
        return
    data = _imported_files_data.get(module_name, {})
    file_vars = data.get("variables", set())
    file_funcs = data.get("functions", [])
    for var in file_vars:
        if var in variables:
            del variables[var]
    for f in file_funcs:
        if f in fun_list:
            fun_list.remove(f)
    _imported_files.remove(module_name)
    _imported_files_data.pop(module_name, None)
