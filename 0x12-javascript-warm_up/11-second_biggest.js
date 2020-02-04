#!/usr/bin/node
/* process.argv return the arguments
the first argument is always node
the second is the executable file
the third is the first argument

slice get a new array from the position selected
*/
let x = 0;
const list = process.argv.slice(2);
const list2 = [];
x = process.argv.length;
if (x <= 2 || x === 3) {
  console.log(0);
} else {
  let count = 0;
  /* get the max value */
  let value = Math.max.apply(null, list);
  for (; count < list.length; count++) {
    if (list[count] === value) {
      delete list[count];
      break;
    }
  }
  /* create the new list without the empty element */
  count = 0;
  for (; count < list.length; count++) {
    if (list[count]) {
      list2.push(list[count]);
    }
  }
  console.log(list2);
  /* once we delete the biggest we get the second one */
  value = Math.max.apply(null, list2);
  console.log(value);
}
