#!/usr/bin/node
let i = 0;
const argNum = process.argv;
if (argNum.length === 2) {
  console.log('Missing number of occurrences');
} else {
  while (i < argNum[2]) {
    console.log('C is fun');
    i++;
  }
}
