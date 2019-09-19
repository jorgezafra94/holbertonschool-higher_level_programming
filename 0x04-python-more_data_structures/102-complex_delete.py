#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lista = []
    num = 0
    for element in a_dictionary:
        if (a_dictionary[element] == value):
            lista.append(element)
    for i in range(len(lista)):
        del a_dictionary[lista[i]]
    return (a_dictionary)
