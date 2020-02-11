#!/usr/bin/node
/* module request */
const request = require('request');
let counter = 0;
const users = [];
const number = [];
const page = process.argv[2];
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const lista = JSON.parse(body);
    for (const user of Object.values(lista)) {
      users.push(user.userId);
    }
    let keys = new Set(users);
    keys = Array.from(keys);
    for (const id of Object.values(keys)) {
      counter = 0;
      for (const obj of Object.values(lista)) {
        if (id === obj.userId && obj.completed === true) {
          counter++;
        }
      }
      number.push(counter);
    }
    const result = {};
    for (let i = 0; i < keys.length; i++) {
      result[keys[i]] = number[i];
    }
    console.log(result);
  }
});
