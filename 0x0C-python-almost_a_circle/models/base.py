#!/usr/bin/python3
"""
main class of all the proyect

"""

# import turtle
import csv
import os
import json


class Base:
    """ class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        if id is None increment the private class attribute __nb_objects
        else asign to self.id the value of id

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """  to_json_string: return an object in json format"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """  save_to_fie: save in a fil the dicts of each instance passed"""
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

    @staticmethod
    def from_json_string(json_string):
        """  from_json_string: return an object from a json string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        create: create a new instance depending of the cls.__name__
        it is necesary to initialize the variables width, height
        if it is Rectangle or size if it is Square
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        load_from_file: reads fro file.json and returns the objects
        """
        filename = cls.__name__ + ".json"
        variable = ""
        result = []
        inst = []
        if os.path.exists(filename) is True:
            with open(filename, 'r') as fd:
                variable = fd.read()
                result = cls.from_json_string(variable)
                for elem in result:
                    inst.append(cls.create(**elem))
            return(inst)
        else:
            return (result)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv: save a dir in a csv file
        """
        filename = cls.__name__ + ".csv"
        result = ""
        new = []
        big = []
        with open(filename, 'w') as fd:
            if list_objs is None:
                result = csv.writer(fd, delimiter=',')
                result.writerow([])
            else:
                result = csv.writer(fd, delimiter=',')
                if cls.__name__ == "Rectangle":
                    for elem in list_objs:
                        new = ['id', 'width', 'height', 'x', 'y']
                        var = []
                        for i in new:
                            var.append(getattr(elem, i))
                        result.writerow(var)
                if cls.__name__ == "Square":
                    for elem in list_objs:
                        new = ['id', 'size', 'x', 'y']
                        var = []
                        for i in new:
                            var.append(getattr(elem, i))
                        result.writerow(var)

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv: loads froom csv file and create objects
        """
        filename = cls.__name__ + ".csv"
        inst = []
        d = {}
        if os.path.exists(filename) is True:
            with open(filename) as fd:
                result = csv.reader(fd, delimiter=',')
                for row in result:
                    a = []
                    for elem in row:
                        a.append(int(elem))

                    if cls.__name__ == "Rectangle":
                        new = ['id', 'width', 'height', 'x', 'y']
                        for i in range(len(a)):
                            d[new[i]] = a[i]
                        inst.append(cls.create(**d))
                    if cls.__name__ == "Square":
                        new = ['id', 'size', 'x', 'y']
                        for i in range(len(a)):
                            d[new[i]] = a[i]
                        inst.append(cls.create(**d))
            return(inst)
        else:
            return(result)
"""
    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle = turtle.Turtle()
        for elem in list_rectangles:
            turtle.goto(elem.x, elem.y)
            for i in range(2):
                turtle.up()
                turtle.forward(elem.width)
                turtle.left(90)
                turtle.forward(elem.height)
                turtle.left(90)
            turtle.hidde()

        for elem in list_squares:
            turtle.goto(elem.x, elem.y)
            for i in range(2):
                turtle.up()
                turtle.forward(elem.width)
                turtle.left(90)
                turtle.forward(elem.width)
                turtle.left(90)
            turtle.hidde()
        turtle.done()
"""
