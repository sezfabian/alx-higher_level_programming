#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf8', (error, data) => {
  if (data) {
    console.log(data);
  }
  if (error) {
    console.log(error);
  }
});
