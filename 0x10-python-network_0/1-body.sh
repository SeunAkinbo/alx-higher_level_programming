#!/bin/bash
# The script takes in the URL, sends a GET request, and displays the body of the response
curl -s -w "%{http_code}\n" -o /dev/null "$1" | grep -q 200 && curl -s "$1"
