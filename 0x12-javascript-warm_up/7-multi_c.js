#!/usr/bin/node
const first = 'C is fun';
let number = process.argv[2];
number = parseInt(number);
let count = 0;
if (!number) {
  console.log('Missing number of occurrences');
} else {
  for (; count < number; count++) {
    console.log(first);
  }
}
