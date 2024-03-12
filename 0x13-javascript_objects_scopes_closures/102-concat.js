#!/usr/bin/node

const fs = require('fs');

function errHandler(err) {
  if (err) {
    console.error("Error:", err);
    process.exit(1);
  }
}

const pathList = process.argv.slice(2);
if (pathList.length < 3) {
  console.error("Usage: ./102-concat fileA fileB fileC");
  process.exit(1);
}

const filePathA = pathList[0];
const filePathB = pathList[1];
const destPathC = pathList[2];

fs.readFile(filePathA, 'utf8', (err, dataA) => {
  errHandler(err);
  
  fs.readFile(filePathB, 'utf8', (err, dataB) => {
    errHandler(err);
    
    const concatData = `${dataA}\n${dataB}`;
    fs.writeFile(destPathC, concatData, (err) => {
      handleError(err);
    });
  });
});



/*
const fileACont = fs.readFileSync(filePathA, 'utf8');
const fileBCont = fs.readFileSync(filePathB, 'utf8');
const concatData = fileACont + '\n' + fileBCont;
fs.writeFileSync(destPathC, concatData);
*/
