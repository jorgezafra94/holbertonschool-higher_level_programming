#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    lista = list(a_dictionary)
    if (lista.count(key) > 0):
        del a_dictionary[key]
    return (a_dictionary)
