#!/usr/bin/env bash
# The script takes a URL, sends a request to that URL,
# and displays the size of the body of the response

# Check if a URL argument is provided
if [ $# -eq 0 ];
then
	"Error: Please provide a URL as argument"
	exit 1
fi

# Get the URL from the first argument
URL=$1

# Use curl to fetch the response
RESPONSE_FILE=$(mktemp)
curl -sSLw "%{size_download}" -o "$RESPONSE_FILE" "$URL" > /dev/null

# Print the response size in byte
SIZE=$(cat "$RESPONSE_FILE")
echo $SIZE

# Clean up temporary file
rm "$RESPONSE_FILE"
