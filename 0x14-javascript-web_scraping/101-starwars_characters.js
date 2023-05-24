#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/people';
const end = '/' + id + '/';

function fetchData (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const content = JSON.parse(response.body);
      for (const character of content.results) {
        for (const film of character.films) {
          if (film.endsWith(end)) {
            console.log(character.name);
          }
        }
      }
      url = content.next;
      if (url !== null) {
        fetchData(url); // Fetch the next page of results
      }
    }
  });
}

fetchData(url);
