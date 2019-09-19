#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    big = 0
    name = ""
    if a_dictionary is None:
        return 
    for element in a_dictionary:
        if len(a_dictionary) == 0:
            return None
        if num == 0:
            big = a_dictionary[element]
        if big < a_dictionary[element]:
            big = a_dictionary[element]
            name = (list(a_dictionary))[num]
        num = num + 1
    return (name)
