#!/bin/bash
# add new things with keys and values
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
