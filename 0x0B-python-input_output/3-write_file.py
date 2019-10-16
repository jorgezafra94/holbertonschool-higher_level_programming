#!/usr/bin/python3
"""
function that overwrite the content of a file.
and if the file is not created it is created automatically
"""


def write_file(filename="", text=""):
    number = 0
    with open(filename, 'w') as fd:
        number = fd.write(text)
    return (number)
