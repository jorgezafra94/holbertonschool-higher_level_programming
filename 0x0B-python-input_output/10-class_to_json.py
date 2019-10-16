#!/usr/bin/python3
"""
create a json from a object of a class
"""


def class_to_json(obj):
    import json

    new = json.dumps(obj.__dict__)
    new = json.loads(new)
    return (new)
