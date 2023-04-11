#!/usr/bin/node

const args = process.argv.slice(2);

const numArg = Number(args[0]);

// eslint-disable-next-line no-restricted-globals
if (isNaN(numArg) === false) {
  console.log(`My number: ${numArg}`);
} else {
  console.log('Not a number');
}
