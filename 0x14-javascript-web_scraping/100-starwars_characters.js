#!/usr/bin/node
/* module request */
const request = require('request');
let page = 'https://swapi.co/api/films/';
page += process.argv[2];
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const lista = JSON.parse(body);
    for (const person of Object.values(lista.characters)) {
      const request2 = require('request');
      request2(person, function (err, st, bd) {
        if (err) {
          console.error(err);
        } else {
          const lista2 = JSON.parse(bd);
          console.log(lista2.name);
        }
      });
    }
  }
});
