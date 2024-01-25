#!/bin/bash
#  takes in a URL, sends a GET request to URL, & displays the body of response
curl -sLX GET $1
