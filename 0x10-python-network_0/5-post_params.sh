#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body
curl -s $1 -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD'
