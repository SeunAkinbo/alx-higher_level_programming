#!/bin/bash
# The script takes the URL and displays all the HTTP methods the server will accept
#!/bin/bash
curl -s -i -X OPTIONS "$1" | grep "Allow" | cut -d ":" -f 2- | tr -d '[:space:]'
