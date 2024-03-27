#!/bin/bash
# The script takes the URL and displays all the HTTP methods the server will accept
curl -X OPTIONS -I "$1" | grep -i '^Allow:' | awk '{print $2}'
