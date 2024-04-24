#!/usr/bin/node
// Getting HTTP response status code

const request = require('request');

function getRequestStatusCode (url) {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }
    console.log(`code: ${response.statusCode}`);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <url>');
  process.exit(1);
}

const url = process.argv[2];
getRequestStatusCode(url);
