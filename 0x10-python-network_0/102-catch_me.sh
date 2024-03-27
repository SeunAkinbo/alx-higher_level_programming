#!/bin/bash
# The script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -s -X PUT -H "Origin:You got me!" -L 0.0.0.0:5000/catch_me
