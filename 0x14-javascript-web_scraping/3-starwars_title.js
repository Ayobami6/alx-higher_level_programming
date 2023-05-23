#!/usr/bin/node
const request = require('request');

function movieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  });
}

const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('No id passed');
} else {
  const movieId = args[0];
  movieTitle(movieId);
}
