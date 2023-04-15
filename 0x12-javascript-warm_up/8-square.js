#!/usr/bin/node
const process = require('process');
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  let mystring = '';
  for (let i = 1; i <= process.argv[2]; i++) {
    for (let i = 1; i <= process.argv[2]; i++) {
      mystring += '#';
    }
    mystring += '\n';
  }
  console.log(mystring);
}
