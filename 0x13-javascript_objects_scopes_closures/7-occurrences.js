#!/usr/bin/node
/* creating a function */
exports.nbOccurences = function (list, searchElement) {
  const tamaño = list.length;
  let result = 0;
  for (let i = 0; i < tamaño; i++) {
    if (list[i] === searchElement) {
      result += 1;
    }
  }
  return (result);
};
