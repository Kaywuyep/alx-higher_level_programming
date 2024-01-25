#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_m & mk d server respond with a msg
curl -s -X POST 0.0.0.0:5000/catch_me -d "user_id=98" -w "You got me!\n" -o /dev/null
