#!/bin/bash
# script takes a URL, sends request to URL, & displays the size of d body
curl -sI "$1" | grep content-length | awk '{print $2}'
