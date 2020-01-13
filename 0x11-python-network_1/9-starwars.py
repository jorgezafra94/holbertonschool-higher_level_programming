#!/usr/bin/python3
""" getting info from Star Wars API
"""

if __name__ == "__main__":
    import sys
    import requests
    API = "https://swapi.co/api/people/?search="
    complete_API = API + sys.argv[1]
    r = requests.get(complete_API)
    results = r.json()['results']
    print("Number of results: {}".format(len(results)))
    for elem in results:
        print(elem["name"])
