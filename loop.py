from exp_engine import safe_eval

stack = []
top = -1

class LoopContext:
    def __init__(self):
        self.cond = None
        self.start_loop = None
        self.end_loop = None

class loop_node:
    def __init__(self, line):
        self.line = line
        self.next = None

def evaluate_condition(cond, variables):
    try:
        return safe_eval(cond, variables)
    except:
        return False

def loop(text):
    global top
    ctx = LoopContext()
    ctx.cond = text.strip()
    stack.append(ctx)
    top += 1

def add_loop(text):
    global top
    if top < 0:
        return
    c = loop_node(text)
    ctx = stack[top]
    if ctx.start_loop is None:
        ctx.start_loop = ctx.end_loop = c
    else:
        ctx.end_loop.next = c
        ctx.end_loop = c

def eval_loop(func, variables):
    global top
    if top < 0:
        return
    ctx = stack[top]
    start_loop = ctx.start_loop
    try:
        while evaluate_condition(ctx.cond, variables):
            temp = start_loop
            while temp:
                func(temp.line)
                temp = temp.next
    except KeyboardInterrupt:
        pass
    ctx.start_loop = None
    ctx.end_loop = None
    stack.pop()
    top -= 1
