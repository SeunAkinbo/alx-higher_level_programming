#!/bin/bash
# The script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sL -X PUT -H "Origin:HolbertonSchool" -d "status=You got me!" 0.0.0.0:5000/catch_me
