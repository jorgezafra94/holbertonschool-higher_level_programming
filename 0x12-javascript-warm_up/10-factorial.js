#!/usr/bin/node
/* recursion */
const input1 = parseInt(process.argv[2]);
let result = 0;
function recursion (a) {
  if (!a) {
    return (1);
  } else {
    return (a * recursion(a - 1));
  }
}
result = recursion(input1);
console.log(result);
