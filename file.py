import os
from editor import *

def file_exist(code):
    if len(code) == 0:
        print(f"\033[33m::\033[31mError\033[33m::\033[35mfile \033[32m not found !")
        return
    file_name = code[0]
    if os.path.exists(file_name):
        print(f'\033[36m{file_name} is exist\033[0m')
    else:
        print(f'\033[31m{file_name} is not exist\033[0m')

def file_read(code):
    if len(code)==0:
        print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax error !")
        return
    file_name = code[0]
    if (len(code)==1):
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                print("\033[36m"+f.read())
        else:
            print(f"\033[33m::\033[31mError\033[33m::\033[35m{file_name} \033[32m not found !")
        return
    var = code[1]
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return [var, f.read()]
    else:
        print(f"\033[33m::\033[31mError\033[33m::\033[35m{file_name} \033[32m not found !")

def file_write(code, variables):
    if len(code) == 0:
        print(f"\033[33m::\033[31mError\033[33m::\033[35mfile \033[32m not found !")
        return
    if len(code) == 1:
        editor(code[0])
        return
    file_name = code[0]
    var = code[1]
    if var not in variables:
        print(f"\033[33m::\033[31mError\033[33m::\033[35mvariable '\033[33m{var}\033[35m' not found!")
        return
    with open(file_name, "a") as f:
        f.write(str(variables[var]))

def file_copy(code):
    if len(code) < 2:
        print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax error !")
        return
    file_name1 = code[0]
    file_name2 = code[1]
    if not os.path.exists(file_name1):
        print(f"\033[33m::\033[31mError\033[33m::\033[35m{file_name1} \033[32m not found !")
        return
    try:
        with open(file_name1, "r") as f:
            with open(file_name2, "w") as g:
                g.write(f.read())
    except Exception as e:
        print(f"\033[33m::\033[31mError\033[33m::\033[35m{e}")
