#!/usr/bin/node

// a simple function that returns the reversed version of a list:
exports.esrever = function (list) {
  const reversed = []; // the reversed list
  for (let index = list.length - 1; index >= 0; index--) {
    reversed.push(list[index]);
  }
  return reversed;
};
