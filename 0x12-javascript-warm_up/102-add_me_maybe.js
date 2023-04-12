#!/usr/bin/node

// eslint-disable-next-line func-names
exports.addMeMaybe = function (number, theFunction) {
// eslint-disable-next-line no-param-reassign
  theFunction(++number);
};
