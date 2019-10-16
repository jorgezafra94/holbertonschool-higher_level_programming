#!/usr/bin/python3
"""
Write a function that writes an Object to a text file
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    import json

    with open(filename, 'w') as fd:
        new = json.dumps(my_obj)
        fd.write(new)
