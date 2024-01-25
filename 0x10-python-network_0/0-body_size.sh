#!/bin/bash
# script takes a URL, sends request to URL, & displays the size of d body
curl -sI $1 | grep Content-Length | awk '{print $2}'
