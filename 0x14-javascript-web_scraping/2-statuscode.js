#!/usr/bin/node
const request = require('request');

function statusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.log(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('No url passed!');
} else {
  const url = args[0];
  statusCode(url);
}
