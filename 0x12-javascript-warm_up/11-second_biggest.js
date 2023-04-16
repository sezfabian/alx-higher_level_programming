#!/usr/bin/node
const process = require('process');
const argSize = process.argv.length;
let maxNum = 0;
let secNum = 0;
for (let i = 2; i < argSize; i++) {
  if (parseInt(process.argv[i]) > maxNum && argSize > 3) {
    secNum = maxNum;
    maxNum = parseInt(process.argv[i]);
  }
}
console.log(secNum);
