#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

function getCharacterNameInOrder (movieId) {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  // get characters names from api in the right order
  request.get(apiUrl, function (error, body) {
    if (error) {
      console.log(error);
    } else {
      const characters = JSON.parse(body).characters;
      for (let i = 0; i < characters.length; i++) {
        request.get(characters[i], function (error, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}

if (args[0]) {
  const movieId = args[0];
  getCharacterNameInOrder(movieId);
}
