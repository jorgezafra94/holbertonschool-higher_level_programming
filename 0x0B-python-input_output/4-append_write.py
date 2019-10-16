#!/usr/bin/python3
"""
function that append the content of a file.
and if the file is not created it is created automatically
"""


def append_write(filename="", text=""):
    number = 0
    with open(filename, 'a') as fd:
        number = fd.write(text)
    return (number)
