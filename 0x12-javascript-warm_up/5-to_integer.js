#!/usr/bin/node
const process = require('process');
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log(myNum);
}
