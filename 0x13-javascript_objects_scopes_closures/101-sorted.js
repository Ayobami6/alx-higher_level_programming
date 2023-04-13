#!/usr/bin/node

const dict = require('./101-data.js').dict;

const userByOccurrences = {};
for (const id in dict) {
  // occurrences
  const occurrences = dict[id];
  // if the occurrences key has not value yet
  if (!userByOccurrences[occurrences]) {
    userByOccurrences[occurrences] = [];
  }
  // push the old dict key as value to the list value of the occurrence key in the new key
  userByOccurrences[occurrences].push(id);
}

console.log(userByOccurrences);
