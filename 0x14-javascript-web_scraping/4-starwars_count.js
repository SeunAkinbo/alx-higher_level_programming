#!/usr/bin/node
// Gets Starwars Character ID

const request = require('request');

function countMoviesWithCharacter (apiUrl, characterId) {
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    } else if (response.statusCode !== 200) {
      console.log(`Error: ${response.statusCode}`);
      return;
    }
    const movieData = JSON.parse(body);
    const moviesWithCharacter = movieData.results.filter(movie =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(`${moviesWithCharacter.length}`);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
countMoviesWithCharacter(apiUrl, 18);
