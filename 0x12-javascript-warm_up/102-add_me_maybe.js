#!/usr/bin/node
/* function that uses the arguments */
exports.addMeMaybe = function (va, func) {
  va = va + 1;
  func(va);
};
