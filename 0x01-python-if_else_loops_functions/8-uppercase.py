#!/usr/bin/python3
def uppercase(str):
    tam = len(str)
    for i in range(0, tam):
        asci = ord(str[i])
        if asci >= 97 and asci <= 122:
            asci = asci - 32
        print("{:c}".format(asci), end="")
    print("")
