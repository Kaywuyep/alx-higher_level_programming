#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: concat-files.js <fileA> <fileB> <destination>');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

const fileAContent = fs.readFileSync(fileAPath, 'utf-8');
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');

const concatenatedContent = `${fileAContent}${fileBContent}`;

fs.writeFileSync(destinationPath, concatenatedContent);

console.log(`Files ${fileAPath} and ${fileBPath} have been concatenated to ${destinationPath}`);
