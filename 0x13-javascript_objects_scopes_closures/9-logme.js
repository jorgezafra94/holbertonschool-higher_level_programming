#!/usr/bin/node
/* USING SCOPE FOR GET GLOBAL VARIABLES */
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter += 1;
};
