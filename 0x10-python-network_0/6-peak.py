#!/usr/bin/python3
""" find the peak
"""


def find_peak(list_of_integers):
    """ function that get the peak from a list
    """
    if not list_of_integers:
        return (None)
    lista = list_of_integers
    for i in range(len(lista)):
        if i == 0:
            aux = lista[i]
        if i != 0 and i != len(lista) - 1:
            if lista[i] >= aux:
                aux = lista[i]
            if lista[i] >= lista[i - 1] and lista[i] >= lista[i + 1]:
                return(lista[i])
    return (aux)
