#!/usr/bin/node
/* calling x times a function */
exports.callMeMoby = function (times, func) {
  let count = 0;
  for (; count < times; count++) {
    func();
  }
};
