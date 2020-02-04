#!/usr/bin/node
/* create a adding function */
const input1 = parseInt(process.argv[2]);
const input2 = parseInt(process.argv[3]);
function add (a, b) {
  let result = 0;
  result = a + b;
  console.log(result);
}
add(input1, input2);
