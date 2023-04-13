#!/usr/bin/node

exports.converter = function (base) {
  return function (numArg) {
    return numArg.toString(base);
  };
};
