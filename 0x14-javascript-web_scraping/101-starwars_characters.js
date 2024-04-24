#!/usr/bin/node
const request = require('request');

const fetchMovieCharacters = (movieId) => {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      fetchCharactersDetails(characters, 0);
    } else {
      console.error('Error fetching movie data:', error || 'Invalid response');
    }
  });
};

const fetchCharactersDetails = (characterUrls, index) => {
  if (index >= characterUrls.length) return;

  request(characterUrls[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharactersDetails(characterUrls, index + 1);
    } else {
      console.error('Error fetching character data:', error || 'Invalid response');
    }
  });
};

// Check if Movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
fetchMovieCharacters(movieId);
