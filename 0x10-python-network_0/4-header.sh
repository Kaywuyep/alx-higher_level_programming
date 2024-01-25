#!/bin/bash
# takes urls as arg, sends a GET request to the URL, and displays the body
curl -s $1 -X GET -H "X-School-User-Id: 98"
