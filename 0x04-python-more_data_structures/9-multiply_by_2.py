#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for ele in a_dictionary:
        new[ele] = (a_dictionary[ele] * 2)
    return new
