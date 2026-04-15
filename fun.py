fun_list = []
fun_stack = []
fun_top = -1

class FunLine:
    def __init__(self, line):
        self.line = line
        self.next = None

class Function:
    def __init__(self, name):
        self.name = name.strip()
        self.start = None
        self.end = None

def fun(text):
    global fun_top
    name = text.strip()
    f = Function(name)
    fun_stack.append(f)
    fun_top += 1

def add_fun(text):
    global fun_top
    if fun_top < 0:
        return
    node = FunLine(text)
    ctx = fun_stack[fun_top]
    if ctx.start is None:
        ctx.start = ctx.end = node
    else:
        ctx.end.next = node
        ctx.end = node

def end_fun():
    global fun_top
    if fun_top < 0:
        return
    f = fun_stack[fun_top]
    fun_list.append(f)
    fun_stack.pop()
    fun_top -= 1

def find_fun(name):
    for f in fun_list:
        if f.name == name:
            return f
    return None

def call_fun(name, eval_func):
    f = find_fun(name)
    if not f:
        print(f"\033[33m::\033[31mError\033[33m::\033[35m function '{name}' not found!\033[0m")
        return
    temp = f.start
    while temp:
        eval_func(temp.line)
        temp = temp.next

