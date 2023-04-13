#!/usr/bin/node
const process = require('process');
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= myNum; i++) {
    console.log('C is fun');
  }
}
