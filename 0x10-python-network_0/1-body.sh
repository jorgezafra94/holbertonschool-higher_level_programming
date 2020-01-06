#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
code=$(curl -sI "$1"| grep "HTTP" | cut -d' ' -f2); [ "$code" -eq 200 ] && curl -s "$1"
