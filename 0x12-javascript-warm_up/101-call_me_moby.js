#!/usr/bin/node

// eslint-disable-next-line func-names
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
