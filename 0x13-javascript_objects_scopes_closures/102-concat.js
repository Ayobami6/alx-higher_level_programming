#!/usr/bin/node
const fs = require('fs');

const fileOne = fs.readFileSync(process.argv[2]).toString();
const fileTwo = fs.readFileSync(process.argv[3]).toString();

const destinationFile = process.argv[4];

fs.writeFileSync(destinationFile, fileOne + fileTwo);
