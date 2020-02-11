#!/usr/bin/node
/* module request */
const request = require('request');
const page = process.argv[2];
const dicti = {};
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const lista = JSON.parse(body);
    for (const task of Object.values(lista)) {
      if (task.completed) {
        if (dicti[task.userId]) {
          dicti[task.userId] += 1;
        } else {
          dicti[task.userId] = 1;
        }
      }
    }
    console.log(dicti);
  }
});
