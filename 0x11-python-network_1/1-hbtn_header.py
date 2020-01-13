#!/usr/bin/python3
""" get headers from web-site
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
