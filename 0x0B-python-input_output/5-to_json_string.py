#!/usr/bin/python3
"""
create the json-string from an object
"""


def to_json_string(my_obj):
    import json

    return json.dumps(my_obj)
