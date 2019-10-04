#!/usr/bin/python3
"""

"""


def text_indentation(text):
    """
    Args
    """
    cont = 0
    new = ""
    for i in text:
        if i == " " and cont == 0:
            continue
        else:
            if i in "?.:":
                new = new + i + "\n" + "\n"
                cont = 0
            else:
                new = new + i
                cont = cont + 1
    rev = ''.join(reversed(new))
    new = ""
    cont = 0
    for i in rev:
        if i == " " and cont == 0:
            continue
        else:
            new = new + i
            cont = cont + 1
    new = ''.join(reversed(new))
    print(new, end="")
