#!/usr/bin/node
// Prints all characters of a Star Wars movie:

const request = require('request');

function printMovieCharacters (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data: ${error}`);
    } else if (response.statusCode !== 200) {
      console.error(`Error: Received status code ${response.statusCode} from API`);
    } else {
      const movieData = JSON.parse(body);
      movieData.characters.forEach(characterUrl => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(`Error fetching character data: ${charError}`);
          } else if (charResponse.statusCode !== 200) {
            console.error(`Error: Received status code ${charResponse.statusCode} for character`);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

// Check if Movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
printMovieCharacters(movieId);
