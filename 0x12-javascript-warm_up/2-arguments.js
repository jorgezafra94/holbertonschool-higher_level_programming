#!/usr/bin/node
/* process.argv return the arguments
the first argument is always node
the second is the executable file
the third is the first argument
*/
let x = 0;
x = process.argv.length;
if (x <= 2) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
