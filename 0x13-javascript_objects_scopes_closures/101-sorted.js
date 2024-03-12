#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
Object.keys(dict).forEach(key => {
  const value = dict[key];
  if (newDict[value]) {
    newDict[value].push(key);
  } else { newDict[value] = [key]; }
});

console.log(newDict);
