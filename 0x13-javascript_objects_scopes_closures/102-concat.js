#!/usr/bin/node

const fileSystem = require('fs');

const filePath = process.argv.slice(2);

const fileDataA = fileSystem.readFile(filePath[0], 'utf8');
const fileDataB = fileSystem.readFile(filePath[1], 'utf8');
fileSystem.writeFile(filePath[2], fileDataA + fileDataB);
