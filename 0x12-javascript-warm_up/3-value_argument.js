#!/usr/bin/node
/* process.argv return the arguments
the first argument is always node
the second is the executable file
the third is the first argument

*/
let x = 0;
x = process.argv[2];
if (x) {
  console.log(x);
} else {
  console.log('No argument');
}
