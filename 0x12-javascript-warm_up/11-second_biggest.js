#!/usr/bin/node
const process = require('process');
const argSize = process.argv.length;
if (argSize > 3) {
  const myNums = process.argv.map(Number).slice(2, argSize).sort((a, b) => a - b);
  console.log(myNums[argSize - 4]);
} else {
  console.log(0);
}
