from exp_engine import safe_eval

variables = {}

def exp(code):
    var = code.pop(0)
    code.pop(0)
    expr = ' '.join(code)
    try:
        variables[var] = safe_eval(expr, variables)
    except:
        print("\033[33m::\033[31mError\033[33m::\033[35minvalid expression !")
        exit()
