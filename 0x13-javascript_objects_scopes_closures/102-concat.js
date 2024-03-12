#!/usr/bin/node

const pathList = process.argv.slice(2);

const fs = require('fs');

const fpA = pathList[0];
const fpB = pathList[1];
const dpC = pathList[2];

const fileACont = fs.readFileSync(fpA, 'utf8');
const fileBCont = fs.readFileSync(fpB, 'utf8');
const concat = fileACont + '\n' + fileBCont;

fs.writeFileSync(dpC, concat);
