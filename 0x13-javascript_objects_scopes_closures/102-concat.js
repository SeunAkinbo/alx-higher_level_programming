#!/usr/bin/node

const fileSystem = require('fs');

const filePath = process.argv.slice(2);

const fileDataA = fileSystem.readFileSync(filePath[0], 'utf8');
const fileDataB = fileSystem.readFileSync(filePath[1], 'utf8');
fileSystem.writeFileSync(filePath[2], fileDataA + fileDataB);
