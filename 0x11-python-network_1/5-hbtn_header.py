#!/usr/bin/python3
""" get headers and print the value of x-request-id
"""
if __name__ == "__main__":
    import sys
    import requests
    r = requests.get(sys.argv[1])
    # mirar contenido con r.__dict__
    # get es como r.__dict__['headers']
    headers = r.__dict__.get('headers')
    id = headers.get('x-request-id')
    print(id)
