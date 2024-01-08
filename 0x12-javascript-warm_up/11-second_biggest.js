#!/usr/bin/node
const List = process.argv.slice(2);
if (!List.sort((a, b) => b - a)[1]) {
  console.log(0);
} else {
  console.log(List.sort((a, b) => b - a)[1]);
}
