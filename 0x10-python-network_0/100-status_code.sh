#!/bin/bash
# get status code without use ; and && or any pipe, redirection, etc.
curl -s -o /dev/null "$1" -w "%{http_code}"
