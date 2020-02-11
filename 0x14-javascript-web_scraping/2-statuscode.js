#!/usr/bin/node
/* module request */
const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response.statusCode);
});
