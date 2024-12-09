#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.log('Movie ID is required');
  process.exit(1);
}

// URL for the films endpoint with the provided movie ID
const url = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Failed to retrieve data for movie ID:', movieId);
    return;
  }

  // Parse the response body into JSON
  const movieData = JSON.parse(body);

  // Get the list of character URLs from the movie data
  const characterUrls = movieData.characters;

  // Iterate over each character URL and fetch the character data
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.log('Failed to retrieve character data');
        return;
      }

      // Parse the character data and print the character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
