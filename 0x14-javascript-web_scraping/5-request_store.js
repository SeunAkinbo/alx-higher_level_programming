#!/usr/bin/node
// Scrapes the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

function fetchWebPageContent (url, filePath) {
  request.get(url, { encoding: 'utf-8' }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.log(`Error: ${response.statusCode}`);
    } else {
      fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}

// Check if URL and file path are provided as command-line arguments
if (process.argv.length !== 4) {
  console.log('Usage: node script.js <url> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];
fetchWebPageContent(url, filePath);
