from variables import exp

from display import display

from get import get

from system import system

from pause import pause

import fun

import loop

from variables import variables

def eval_code(code):
    code=code.split(' ')
    t=[]
    for i in range(len(code)):
        if code[i]=='':
            continue
        t.append(code[i].strip())
    code=t
    if len(code)==0:
        return
    if code[0] == "-":
            fun.add_fun(" ".join(code[1:]))
            return
    if code[0] == ".":
            loop.add_loop(" ".join(code[1:]))
            return
    if code[0] == "fun":
            fun.fun(" ".join(code[1:]))
            return
    elif '=' in code:
        exp(code)
    elif code[0]=="display":
        display(code[1:])
    elif code[0]=="get":
        get(code[1:])
    elif code[0]=="$":
        pass
        #my comments
    elif code[0]=="...":
        system(code[1:])
    elif code[0]=="pause":
            if(len(code)==1):
                print(f"\033[33m::\033[31mError\033[33m::\033[4;35msyntax\033[0m\033[32m error !")
            else:
                pause(code[1])
    elif code[0] == "/fun":
            fun.end_fun()
    elif code[0] == "call":
            if(len(code)==1):
                print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax \033[32m error !")
            else:
                fun.call_fun(code[1], eval_code)
    elif code[0] == "loop":
            loop.loop(" ".join(code[1:]))
    elif code[0] == "/loop":
            loop.eval_loop(eval_code,variables)
    elif code[0] == "del":
            from delete import dlt
            if len(code) < 3:
                print("\033[33m::\033[31mError\033[33m:: \033[35msyntax error for del! Usage: del var|fun|file name")
            else:
                dlt(code[1], " ".join(code[2:]))
    elif code[0] == "import":
        from impt import impt
        if len(code) == 1:
            print("\033[33m::\033[31mError\033[33m:: \033[35msyntax error !")
        else:
            impt(" ".join(code[1:]))
    elif code[0] == "export":
        from export import expt
        if len(code) == 1:
            print("\033[33m::\033[31mError\033[33m:: \033[35msyntax error !")
        else:
            expt(" ".join(code[1:]))
    elif code[0] == "exist":
        from file import file_exist
        file_exist(code[1:])
    elif code[0] == "read":
        from file import file_read
        res = file_read(code[1:])
        if res:
            variables[res[0]] = res[1]
    elif code[0] == "write":
        from file import file_write
        file_write(code[1:], variables)
    elif code[0] == "copy":
        from file import file_copy
        file_copy(code[1:])
    else:
        print(f"\033[33m::\033[31mError\033[33m::\033[4;36m{code[0]}\033[0m \033[35m keyword not found !")
        exit()
