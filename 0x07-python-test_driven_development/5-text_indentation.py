#!/usr/bin/python3
"""
  function that prints the text in the correct way
"""


def text_indentation(text):
    """
    Args:
        text: string

    Raises:
        TypeError: text must be a string

    Returns:
        Text separed by \n if finds .?:

    """
    cont = 0
    new = ""
    if not str or type(text) is not str:
        raise TypeError('text must be a string')

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
