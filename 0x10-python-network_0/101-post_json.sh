#!/bin/bash
# POST a Json file
curl -sd "@$2" -X POST -H "Content-Type: application/json" "$1"
