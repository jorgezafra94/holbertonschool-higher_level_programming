#!/bin/bash
# first tap curl -L-s 0.0.0.0:5000/catch_me -X OPTIONS then change OPTIONS by PUT to understand everything
curl -s -L 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin:HolbertonSchool"
