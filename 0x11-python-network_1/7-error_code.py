#!/usr/bin/python3
""" get error status or body if doesnt fails
using requests package
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if (r.status_code < 400):
        # raise_for_status method return None if status 200
        # otherway raise an error
        # r.raise_for_status()
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
