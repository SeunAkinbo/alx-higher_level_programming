#!/usr/bin/node
// Gets Starwars Movies Title

const request = require('request');

function fetchMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    } else if (response.statusCode !== 200) {
      console.log(`Error: ${response.statusCode}`);
      return;
    }
    const movieData = JSON.parse(body);
    console.log(`${movieData.title}`);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
fetchMovieTitle(movieId);
