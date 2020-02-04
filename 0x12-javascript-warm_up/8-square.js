#!/usr/bin/node
let number = process.argv[2];
number = parseInt(number);
let count1 = 0;
let count2 = 0;
let x = '';
if (!number) {
  console.log('Missing size');
} else {
  // create a XXX string depending of the input
  for (; count2 < number; count2++) {
    x = x + 'X';
  }
  // print N times the variable x
  for (; count1 < number; count1++) {
    console.log(x);
  }
}
