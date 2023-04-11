#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const a = Number(args[0]);
const b = Number(args[1]);
add(a, b);
