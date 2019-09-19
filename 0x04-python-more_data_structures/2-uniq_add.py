#!/usr/bin/python3
def uniq_add(my_list=[]):
    var = 0
    if my_list is None:
        return var
    elem = set(my_list)
    elem = list(elem)
    for i in elem:
        var = var + i
    return var
