#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  let n = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    myList[n] = list[i];
    n++;
  }
  return myList;
};
