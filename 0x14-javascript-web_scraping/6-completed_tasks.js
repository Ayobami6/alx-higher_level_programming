#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

function userTaskCompleted (apiUrl) {
  request.get(apiUrl, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const json = JSON.parse(body);
      const completed = {};
      for (const task of json) {
        if (task.completed === true) {
          /* if a new key with no value */
          if (completed[task.userId] === undefined) {
            completed[task.userId] = 1;
            /* if key exists incremen the value of key */
          } else {
            completed[task.userId]++;
          }
        }
      }
      console.log(completed);
    }
  });
}

if (args.length === 1) {
  const apiUrl = args[0];
  userTaskCompleted(apiUrl);
}
