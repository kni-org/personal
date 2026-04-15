from variables import variables
def get(code):
    if len(code)!=1 and code[0]=="<":
        code.pop(0)
        for i in code:
            variables[i]=input("\033[32m")
    else:
        print("\033[33m::\033[31mError\033[33m::\033[4;36msyntax\033[0m\033[35m error !")
