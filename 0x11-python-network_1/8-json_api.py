#!/usr/bin/python3
""" json with requests package
"""

if __name__ == "__main__":
    import requests
    import sys

    value = {'q': ""}

    if (len(sys.argv) > 1):
        value['q'] = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        js = r.json()
        if len(js) == 0:
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except:
        print("Not a valid JSON")
