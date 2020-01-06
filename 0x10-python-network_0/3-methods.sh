#!/bin/bash
# show all methos supported by server
curl -sIX OPTIONS "$1" | grep Allow: | cut -d' ' -f2-
