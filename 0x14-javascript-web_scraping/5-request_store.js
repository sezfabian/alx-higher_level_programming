#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filepath, body, 'utf8', (error) => {
        if (error) {
          console.log(error);
        }
      });
    }
  }
});
