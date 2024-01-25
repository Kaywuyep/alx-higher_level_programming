#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_m & mk d server respond with a msg
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
