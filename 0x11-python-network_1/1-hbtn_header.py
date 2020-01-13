#!/usr/bin/python3
""" get headers from web-site
"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.info()
    print(headers['X-Request-Id'])
