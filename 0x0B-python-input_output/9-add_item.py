#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json') is True:
    lista = list(load_from_json_file("add_item.json"))
    for i in range(1, len(sys.argv)):
        lista.append(sys.argv[i])
    save_to_json_file(lista, "add_item.json")
else:
    lista = []
    save_to_json_file(lista, "add_item.json")
