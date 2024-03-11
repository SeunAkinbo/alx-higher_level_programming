#!/usr/bin/node

const [, ,args] = process.argv;
if (args) {
	console.log(args);
} else {
	console.log('No argument');
}
