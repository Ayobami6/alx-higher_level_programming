#!/usr/bin/node
const fs = require('fs');

/* Function that reads a file */
function fileRead (filePath) {
  fs.readFile(filePath, 'utf-8', (error, content) => {
    if (error) {
      console.log(error);
    } else {
      console.log(content);
    }
  });
}

const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('No args passed!');
} else {
  const filePath = args[0];
  fileRead(filePath);
}
