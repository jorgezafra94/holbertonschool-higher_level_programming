#!/usr/bin/python3
def safe_print_division(a, b):
    flag = 0
    div = 0
    try:
        div = a / b
    except:
        flag = 1
    finally:
        if flag == 0:
            print("Inside result: {}".format(div))
            return (div)
        else:
            print("Inside result: None")
            return (None)
