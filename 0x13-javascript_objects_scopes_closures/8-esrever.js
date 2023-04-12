#!/usr/bin/node

// eslint-disable-next-line func-names
exports.esrever = function (list) {
  const revList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
