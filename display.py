from variables import variables
from exp_engine import safe_eval

def display(content):
    if not content or content[0] != ">":
        print("\033[33m::\033[31mError\033[33m::syntax error !")
        exit()

    content = content.copy()
    content.pop(0)

    if not content:
        return

    text = ' '.join(content)

    if text.startswith('"') and text.endswith('"'):
        print("\033[36m" + text[1:-1].encode().decode('unicode_escape') + "\033[0m", end="")
    else:
        try:
            result = safe_eval(text, variables)
            print("\033[36m" + str(result) + "\033[0m")
        except:
            print("\033[36m" + text + "\033[0m")
