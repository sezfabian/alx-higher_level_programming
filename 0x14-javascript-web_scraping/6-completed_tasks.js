#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const usersDict = {};
      const content = JSON.parse(response.body);
      for (const task of content) {
        if (task.completed === true) {
          if (usersDict[task.userId] === undefined) {
            usersDict[task.userId] = 0;
          }
          usersDict[task.userId]++;
        }
      }
      console.log(usersDict);
    }
  }
});
