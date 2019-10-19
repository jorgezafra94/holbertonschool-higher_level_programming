#!/usr/bin/python3
"""
main class of all the proyect

"""

import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        if id is None increment the private class attribute __nb_objects
        else asign to self.id the value of id

        * to_json_string: return an object in json format
        * save_to_fie: save in a fil the dicts of each instance passed
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        new = []
        result = ""
        with open(filename, 'w') as fd:
            if list_objs is None:
                result = cls.to_json_string(new)
            else:
                for elem in list_objs:
                    new.append(elem.to_dictionary())
                result = cls.to_json_string(new)
            fd.write(result)
