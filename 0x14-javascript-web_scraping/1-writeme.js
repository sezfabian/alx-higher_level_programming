#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filepath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filepath, content, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
