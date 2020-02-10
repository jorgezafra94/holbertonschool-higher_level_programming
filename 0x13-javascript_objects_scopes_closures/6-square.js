#!/usr/bin/node
/* inheritance in JS */
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
