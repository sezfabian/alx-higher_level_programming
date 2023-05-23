#!/usr/bin/node
const process = require('process');
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const film = JSON.parse(response.body);
      console.log(film.title);
    }
  }
});
