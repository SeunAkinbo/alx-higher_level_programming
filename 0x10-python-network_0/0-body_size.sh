#!/usr/bin/env bash
# The script takes a URL, sends a request to that URL,
# and displays the size of the body of the response

URL=$1

curl -Is "$URL" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
