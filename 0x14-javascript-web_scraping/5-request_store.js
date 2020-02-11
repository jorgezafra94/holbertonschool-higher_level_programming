#!/usr/bin/node
/* save the page */
const request = require('request');
const fs = require('fs');
const page = process.argv[2];
const file = process.argv[3];
request(page, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFileSync(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
