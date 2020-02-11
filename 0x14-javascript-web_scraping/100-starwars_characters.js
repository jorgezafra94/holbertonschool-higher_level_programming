#!/usr/bin/node
/* module request */
const request = require('request');
const req2 = require('request');
let page = 'https://swapi.co/api/films/';
page = page + process.argv[2];
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    let lista = JSON.parse(body);
    lista = lista.characters;
    for (const elem of Object.values(lista)) {
      req2(elem, function (e, s, b) {
        if (e) {
          console.error(e);
        } else {
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
