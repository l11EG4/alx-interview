#!/usr/bin/node
/**
* Prints all characters of a Star Wars movie
* The first positional argument passed is the Movie ID
* Display one character name per line in the same order
* as  list in the /films/ endpoint
* Made by MEGA
*/


const util = require('util');
const request = util.promisify(require('request'));

const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

async function fetchData(url) {
  try {
    const response = await request(url);
    return JSON.parse(response.body);
  } catch (error) {
    throw error;
  }
}

async function CharRequest(idx, characters, limit) {
  try {
    if (idx < limit) {
      const character = await fetchData(characters[idx]);
      console.log(character.name);
      await CharRequest(idx + 1, characters, limit);
    }
  } catch (error) {
    console.error('error:', error);
  }
}

(async () => {
  try {
    const movieData = await fetchData(urlMovie);
    const characters = movieData.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      await CharRequest(0, characters, limit);
    }
  } catch (error) {
    console.log(error);
  }
})();
