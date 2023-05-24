#!/usr/bin/node
const { count } = require('console');
const process = require('process');
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const resp = JSON.parse(response.body);
      let count = 0;
      for (const film of resp.results) {
        for (const character of film.characters) {
          if (character.endsWith('/18/')) {
            count = count + 1;
          }
        }
      }
      console.log(count);
    }
  }
});
