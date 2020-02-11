#!/usr/bin/node
/* module request */
const request = require('request');

const page = 'http://swapi.co/api/films/' + process.argv[2];
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
