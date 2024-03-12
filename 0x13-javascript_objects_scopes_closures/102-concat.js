#!/usr/bin/node

const file = require('fs');

filePath = process.argv.slice(2);

const fileDataA = file.readFileSync(filePath[0], 'utf8');
const fileDataB = file.readFileSync(filePath[1], 'utf8');
file.writeFileSync(filePath[2], fileDataA + fileDataB);
