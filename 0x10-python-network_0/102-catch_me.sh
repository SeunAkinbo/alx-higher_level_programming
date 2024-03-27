#!/bin/bash
# The script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -s -X PUT -d "status=You%20got%20me%21" 0.0.0.0:5000/catch_me
