#!/usr/bin/node
const dict = require('./101-data.js').dict;

const myDict = {};

for (const id in dict) {
  const occurrence = dict[id];

  if (myDict[occurrence] === undefined) {
    myDict[occurrence] = [id];
  } else {
    myDict[occurrence].push(id);
  }
}

console.log(myDict);
