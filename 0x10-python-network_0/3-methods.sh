#!/bin/bash
# show all methos supported by server
curl -LsX OPTIONS "$1"
