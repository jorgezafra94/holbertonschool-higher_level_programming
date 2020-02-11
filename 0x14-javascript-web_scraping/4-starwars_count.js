#!/usr/bin/node
/* module request */
const request = require('request');
let counter = 0;
const page = process.argv[2];
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  }
  const lista = JSON.parse(body);
  for (let i = 0; i < lista.results.length; i++) {
    for (let j = 0; j < lista.results[i].characters.length; j++) {
      if (lista.results[i].characters[j].search('/18/') > 0) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
