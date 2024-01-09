#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (process.argv.length !== 5) {
  console.error('Usage: concat-files.js <fileA> <fileB> <destination>');
  process.exit(1);
}

if (
  !fs.existsSync(fileA) ||
  !fs.statSync(fileA).isFile() ||
  !fs.existsSync(fileB) ||
  !fs.statSync(fileB).isFile() ||
  fileC === undefined
) {
  console.error('Invalid arguments. Please check file paths and ensure destination is provided.');
  process.exit(1);
}

const fileAContent = fs.readFileSync(fileA, 'utf-8');
const fileBContent = fs.readFileSync(fileB, 'utf-8');
const stream = fs.createWriteStream(fileC);

stream.write(fileAContent);
stream.write(fileBContent);
stream.end();

console.log(`Files ${fileA} and ${fileB} have been concatenated to ${fileC}`);
