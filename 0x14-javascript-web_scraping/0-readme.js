#!/usr/bin/node
// Reading data from file

const fs = require('fs');

function readAndPrintFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFileContent(filePath);
