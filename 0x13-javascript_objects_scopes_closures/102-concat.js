#!/usr/bin/node
const args = process.argv;
const FileA = args[2];
const FileB = args[3];
const destinationFile = args[4];
const fs = require('fs');
let contentA;
let contentB;

fs.readFile(FileA, function (err, data) {
  if (err) {
    return console.error(err);
  }
  contentA = data.toString();
  fs.appendFile(destinationFile, contentA, function (err) {
    if (err) throw err;
  });
});

fs.readFile(FileB, function (err, data) {
  if (err) {
    return console.error(err);
  }
  contentB = data.toString();
  fs.appendFile(destinationFile, contentB, function (err) {
    if (err) throw err;
  });
});
