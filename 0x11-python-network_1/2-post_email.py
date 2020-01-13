#!/usr/bin/python3
""" POST a variable with key
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    values = {'email': '{}'.format(sys.argv[2])}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    # data should be bytes
    try:
        with urllib.request.urlopen(sys.argv[1], data) as response:
            # if we use data we are calling POST method
            for i in response:
                # here we get the answer
                print(i.decode('utf-8'))
    except urllib.error.URLError as e:
        print(e.reason)
