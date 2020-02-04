#!/usr/bin/node
/* process.argv return the arguments
the first argument is always node
the second is the executable file
the third is the first argument

*/
let first = ''; let second = '';
first = process.argv[2];
second = process.argv[3];
console.log(first + ' is ' + second);
