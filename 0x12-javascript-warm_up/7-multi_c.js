#!/usr/bin/node
const myVar = 'C is fun';
const x = process.argv[2];

if (typeof parseInt(x) === 'number' && !isNaN(parseInt(x))) {
  for (let n = 0; n < x; n++) {
    console.log(myVar);
  }
} else {
  console.log('Missing number of occurrences');
}
