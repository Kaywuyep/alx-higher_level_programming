#!/bin/bash
# sends a request to a URL passed as an argument, & displays only d status code
curl -sIw '%{http_code}' $1 -o /dev/null
