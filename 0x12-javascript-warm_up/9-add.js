#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const args = process.argv.slice(2);
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

if (isNaN(num1)) {
  console.log('NaN');
} else if (isNaN(num2)) {
  console.log('NaN');
} else {
  add(num1, num2);
}
