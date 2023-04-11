#!/usr/bin/node

const parsedArg = process.argv.slice(2);

const arg = Number(parsedArg[0]);

// eslint-disable-next-line no-restricted-globals
if (isNaN(arg) === false) {
  // eslint-disable-next-line no-plusplus
  for (let j = 0; j < arg; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
