#!/usr/bin/node
const process = require('process');
let myNum = parseInt(process.argv[2]);
if (isNaN(parseInt(process.argv[2]))) {
  myNum = 1;
}
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(myNum));
