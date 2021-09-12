#!/usr/bin/node
// Prints a specified string only if the first argument can be converted to an integer

const args = process.argv;
const number = parseInt(args[2], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
