#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    big = 0
    name = ""
    if a_dictionary is None:
        return None
    for element in a_dictionary:
        if not a_dictionary[element]:
            return None
        if num == 0:
            big = a_dictionary[element]
        if big < a_dictionary[element]:
            big = a_dictionary[element]
            name = (list(a_dictionary))[num]
        num = num + 1
    return (name)
