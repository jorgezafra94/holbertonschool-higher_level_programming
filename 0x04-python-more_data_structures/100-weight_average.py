#!/usr/bin/python3
def weight_average(my_list=[]):
    tup = 0
    numerador = 0
    divisor = 0
    if not my_list:
        return 0
    for tuplas in my_list:
        divisor = divisor + tuplas[1]
        tup = tuplas[0] * tuplas[1]
        numerador = numerador + tup
    return (numerador / divisor)
