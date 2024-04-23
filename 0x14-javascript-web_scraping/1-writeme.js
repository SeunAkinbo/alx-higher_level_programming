#!/usr/bin/node
// Writing content to file

const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
}

if (process.argv.length !== 4) {
  console.log('Usage: node script.js <file_path> <content_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];
writeToFile(filePath, contentToWrite);
