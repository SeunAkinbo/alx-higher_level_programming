#!/usr/bin/bash
# The script takes a URL, sends a request to that URL,and displays the size of the body of the response

curl -Is "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
