#!/usr/bin/python3
""" get the first 10 commits from repo
"""
if __name__ == "__main__":
    import sys
    import requests

    owner = sys.argv[2]
    repo = sys.argv[1]
    API = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(API)
    # the commits are in order from new to old
    for i in range(len(r.json())):
        if (i < 10):
            commit = r.json()[i]
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
