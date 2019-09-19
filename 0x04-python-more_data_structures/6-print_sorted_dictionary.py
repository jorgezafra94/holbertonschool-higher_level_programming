#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) != 0:
        lista = sorted(a_dictionary.keys())
        for i in lista:
            print("{}: {}".format(i, a_dictionary[i]))
