#!/usr/bin/node
const args = process.argv.slice(2);
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  // Print the first argument
  console.log(args[0]);
}
