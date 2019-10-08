#!/usr/bin/python3
def magic_string(list=[]):
    list += [1]
    return(("Holberton, " * (len(list) - 1)) + "Holberton")
