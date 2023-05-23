#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
}

const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('No args passed');
} else {
  const filePath = args[0];
  const content = args[1];
  writeToFile(filePath, content);
}
