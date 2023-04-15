#!/usr/bin/node
const process = require('process');
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    let mystring = '';
    for (let i = 1; i <= process.argv[2]; i++) {
      mystring += '#';
    }
    console.log(mystring);
  }
}
