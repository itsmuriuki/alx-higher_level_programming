#!/usr/bin/node
// Prints the first argument passed to it

const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
