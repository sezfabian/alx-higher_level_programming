#!/usr/bin/node
const process = require('process');
const argSize = process.argv.length;
let maxNum = 0;
let secNum = 0;
if (argSize > 3) {
  for (let i = 2; i < argSize; i++) {
    if (parseInt(process.argv[i]) >= maxNum) {
      secNum = maxNum;
      maxNum = parseInt(process.argv[i]);
    }
  }
}
console.log(secNum);
