#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    big = 0
    name = ""
    if not a_dictionary:
        return None
    for element in a_dictionary:
        if num == 0:
            big = a_dictionary[element]
        if big < a_dictionary[element]:
            big = a_dictionary[element]
            name = (list(a_dictionary))[num]
        num = num + 1
    return (name)
