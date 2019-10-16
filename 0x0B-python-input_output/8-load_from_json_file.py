#!/usr/bin/python3
"""
create an object from a json file
"""


def load_from_json_file(filename):
    import json
    with open(filename) as fd:
        obj = fd.read()
    return(json.loads(obj))
