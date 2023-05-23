#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

function getCharacterName (movieId) {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  request.get(apiUrl, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const json = JSON.parse(body);
      for (const character of json.characters) {
        request.get(character, function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            const json = JSON.parse(body);
            console.log(json.name);
          }
        });
      }
    }
  });
}

if (args.length === 1) {
  const movieId = args[0];
  getCharacterName(movieId);
}
