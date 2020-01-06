#!/bin/bash
# POST a Json file
curl -d "@$2" -X POST -H "Content-Type: application/json" "$1"
