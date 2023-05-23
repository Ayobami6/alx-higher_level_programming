#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

function getCharacterNameInOrder (movieId) {
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
  request.get({ url: apiUrl, json: true }, function (error, response, body) {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const characters = body.characters;
      const promises = characters.map((url) => {
        return new Promise((resolve, reject) => {
          request.get({ url, json: true }, function (error, response, body) {
            if (error) {
              reject(error);
            } else {
              resolve(body.name);
            }
          });
        });
      });

      Promise.all(promises)
        .then((names) => console.log(names.join('\n')))
        .catch((error) => console.error(error));
    } else {
      console.error(`Request failed with status code ${response.statusCode}`);
    }
  });
}

if (args[0]) {
  const movieId = args[0];
  getCharacterNameInOrder(movieId);
}
