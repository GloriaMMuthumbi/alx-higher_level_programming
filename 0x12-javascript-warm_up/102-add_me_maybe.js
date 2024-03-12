#!/usr/bin/node
exports.addMeMAybe = function addMeMaybe (number, theFunction) {
  return theFunction(++number);
};
