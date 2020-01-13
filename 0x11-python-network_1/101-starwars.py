#!/usr/bin/python3
""" getting info from Star Wars API
"""

if __name__ == "__main__":
    import sys
    import requests
    API = "https://swapi.co/api/people/?search="
    complete_API = API + sys.argv[1]
    # go to the first page of the search
    while(1):
        r = requests.get(complete_API)
        prev = r.json().get('previous')
        if not prev:
            break
        else:
            complete_API = prev
    # start from the first page  to the last page
    first = complete_API
    number = 0
    # get the total number of elements
    while(1):
        r = requests.get(complete_API)
        results = r.json().get('results')
        number = number + len(results)
        next = r.json().get('next')
        if not next:
            break
        else:
            complete_API = next
    # now we have to go to the first again and start the printing of info
    complete_API = first
    print("Number of results: {}".format(number))
    while(1):
        r = requests.get(complete_API)
        results = r.json().get('results')
        for elem in results:
            print(elem["name"])
        next = r.json().get('next')
        if not next:
            break
        else:
            complete_API = next
