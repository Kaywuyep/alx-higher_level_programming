#!/usr/bin/node
// Get the value of the first argument
const size = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Print a square of size x using nested loops
  for (let i = 0; i < size; i++) {
    let squareLine = '';
    for (let j = 0; j < size; j++) {
      squareLine += 'X';
    }
    console.log(squareLine);
  }
}
