from eval_code import eval_code
import builtins

def disable_exit(*ags,**kwargs):
    return
builtins.exit=disable_exit

def terminal():
    print(
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mDeveloper :\033[0m \033[37mNiranjan Kumar K\033[0m                   \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mEmail     :\033[0m \033[37mhackerenvironment1514@gmail.com\033[0m    \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mEngine    :\033[0m \033[35mNone\033[0m                               \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mNote      :\033[0m \033[32msystem commands allowed with ...\033[0m   \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n\n"
        "\033[1;34mEnjoy Learning and Practicing!\033[0m\n\n"
        "\033[1;31mExit using:\033[0m \033[37m_exit\033[0m\n"
    )
    
    prompt = "\033[33m::\033[32mk\033m\033[33m::\033[32m$\033[35m "
    statues="on"
    code=''
    
    try:
        while True:
            if statues=="on" and "display" in code:
                print()
            if statues=="on":
                print(prompt,end="")
            code = input().strip()

            if "loop" in code or "fun" in code:
                t=code.split(' ')
                if t[0]!="del":
                    statues="off"

            if "/loop" in code or "/fun" in code:
                statues="on"
            if not code:
                continue
            if code == "_exit":
                break
            
            # Always pass the whole line as string to eval_code
            try :
                eval_code(code)
            except:
                pass
    
    except KeyboardInterrupt:
        print("\n\033[31mKeyboard Interrupt Detected, exiting...\033[0m")
    except Exception as e:
        print(f"\033[31mError in terminal: {e}\033[0m")
    
    print(
        "\n\033[1;32mSuccessfully Exited from K terminal ....     !\033[0m\n\n"
        "\033[1;36mNiranjan Special Thanked, for using Terminal !\033[0m\n")
