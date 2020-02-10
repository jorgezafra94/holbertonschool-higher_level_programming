#!/usr/bin/node
/* inheritance in JS */
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c = 'X') {
    let row = '';
    let count = 0;
    for (; count < this.width; count++) {
      row = row + c;
    }
    for (count = 0; count < this.height; count++) {
      console.log(row);
    }
  }
};
