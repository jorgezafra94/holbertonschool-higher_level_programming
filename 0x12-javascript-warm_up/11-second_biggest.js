#!/usr/bin/node
/* process.argv return the arguments
the first argument is always node
the second is the executable file
the third is the first argument

slice get a new array from the position selected
*/
let x = 0;
const list = process.argv.slice(2);
x = process.argv.length;
if (x <= 2 || x === 3) {
  console.log('0');
} else {
  list.sort();
  console.log(list[list.length - 2]);
}
