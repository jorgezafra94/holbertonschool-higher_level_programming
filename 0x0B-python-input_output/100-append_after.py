#!/usr/bin/python3
"""
function that adds into a file a string, but only after get a match of a string
in this case after match search_string inside the file, we are going to put
the new_string
"""


def append_after(filename="", search_string="", new_string=""):
    result = ""
    with open(filename) as fd:
        for line in fd:
            result = result + line
            if search_string in line:
                result = result + new_string

    with open(filename, "w") as fd:
        fd.write(result)
