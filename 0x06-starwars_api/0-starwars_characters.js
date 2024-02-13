#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2] + '/';
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film information
request(API_URL + filmID, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse the response body to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Iterare through the character URLs and fect character information
  // Make a request to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the charcter nformation and print the character's name Resolve the promise to indicate completion
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
