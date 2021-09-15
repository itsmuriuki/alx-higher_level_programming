#!/usr/bin/node
// Prints the number of arguments already printed and the new
// argument value

let logged = 0;
exports.logMe = function (item) {
  console.log(`${logged}: ${item}`);
  logged++;
};
