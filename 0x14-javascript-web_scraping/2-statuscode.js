#!/usr/bin/node
/* module request */
const request = require('request');

request(process.argv[2], function (response) { // (error, response, body)
  // console.error('error:', error);  Print the error if one occurred
  console.log('code:', response.statusCode); // Print the response status code if a response was received
  // console.log('body:', body);  Print the HTML for the Google homepage.
});
