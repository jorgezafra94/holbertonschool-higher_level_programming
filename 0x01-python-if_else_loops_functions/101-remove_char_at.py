#!/usr/bin/python3
def remove_char_at(str, n):
    tam = len(str)
    j = 0
    arr = ""
    for i in range(tam):
        if (i != n):
            arr = arr + str[i]
        j = j + 1
    return (arr)
