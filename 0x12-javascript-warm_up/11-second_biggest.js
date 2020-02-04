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
  let value = parseInt(list[0]);
  let count = 0;
  let position = 0;
  for (; count < list.length; count++) {
    if (value <= parseInt(list[count])) {
      value = parseInt(list[count]);
      position = count;
    }
  }
  count = 0;
  let second;
  if (position === 0) {
    second = parseInt(list[1]);
  } else {
    second = parseInt(list[0]);
  }
  for (; count < list.length; count++) {
    if (count === position) {
      continue;
    }
    if (second <= parseInt(list[count])) {
      second = parseInt(list[count]);
    }
  }
  console.log(second);
}
