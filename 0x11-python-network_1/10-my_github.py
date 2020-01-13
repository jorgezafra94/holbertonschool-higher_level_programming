#!/usr/bin/python3
""" getting info of account from Github API using credentials
"""

if __name__ == "__main__":
    import sys
    import requests
    user = sys.argv[1]
    pas = sys.argv[2]
    API = "https://api.github.com/users"
    API = API + "/{}".format(user)
    r = requests.get(API, auth=requests.auth.HTTPBasicAuth(user, pas))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print("None")
