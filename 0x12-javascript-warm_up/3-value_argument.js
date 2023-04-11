#!/usr/bin/node

const args = process.argv.slice(2);

// if an arg is passed
if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
