#!/usr/bin/python3
''' getting status code
'''
if __name__ == "__main__":
    import sys
    import urllib.request

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
