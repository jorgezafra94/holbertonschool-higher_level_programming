#!/usr/bin/python3
""" get error status or body if doesnt fails
using requests package
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    try:
        # raise_for_status method return None if status 200
        # otherway raise an error
        r.raise_for_status()
        print(r.text)
    except:
        print("Error Code: {}".format(r.status_code))
