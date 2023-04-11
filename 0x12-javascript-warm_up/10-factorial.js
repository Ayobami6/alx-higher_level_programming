#!/usr/bin/node

const args = process.argv.slice(2);

function fact (n) {
  if (isNaN(n)) return 1;
  if (n === 0) return 1;
  const result = n * fact(n - 1);
  return result;
}

const num = Number(args[0]);

console.log(fact(num));
