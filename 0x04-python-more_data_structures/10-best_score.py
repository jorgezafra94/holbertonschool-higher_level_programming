#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    maxi = 0
    if not a_dictionary:
        return None
    for element in a_dictionary:
        if num == 0:
            maxi = a_dictionary[element]
        if maxi < a_dictionary[element]:
            maxi = a_dictionary[element]
        num = num + 1
    for element in a_dictionary:
        if maxi == a_dictionary[element]:
            return (element)
