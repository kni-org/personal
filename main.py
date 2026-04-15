import colorama
colorama.init()

from sys import argv

import os

import eval_code

import terminal

import editor 

argv.pop(0)

if len(argv)==0:
    print("\033[33m::\033[31mError\033[33m::\033[4;36marguments\033[0m \033[35m not found !")
    exit()
elif argv[0]=="--version":
    print("\033[32m::\033[33mversion\033[32m::\033[4;36m1.0\033[0m")
    exit()
elif argv[0]=="--terminal":
    terminal.terminal()
elif argv[0]=="--file":
    try:
        editor.editor(argv[1])
    except:
        print("\033[33m::\033[31mError\033[33m::\033[4;36mfile\033[0m\033[35m not found !")
elif '.' in argv[0] and argv[0].split('.')[1]=="k" :
    if os.path.exists(argv[0]):
        with open(argv[0],"r") as f :
            lines=f.read().split("\n")
            for i in lines:
                try:
                    eval_code.eval_code(i);
                except :
                    print("\033[33m::\033[31mError\033[33m::\033[4;36msyntax\033[0m\033[35m error !")
                    exit()
    else:
        print(f"\033[33m::\033[31mError\033[33m::\033[4;36m{argv[0]}\033[0m\033[35m not found !")
        exit()
else:
    print("\033[33m::\033[31mError\033[33m::\033[35m invalide \033[4;36marguments\033[0m \033[36m !")
    exit()
