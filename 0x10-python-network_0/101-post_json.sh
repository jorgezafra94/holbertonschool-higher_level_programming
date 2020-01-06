#!/bin/bash
# POST a Json file
curl "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
