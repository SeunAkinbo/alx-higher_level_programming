#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

const args = process.argv.slice(2);
const number = parseInt(args[0]);

console.log(factorial(number));
