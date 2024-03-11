#!/usr/bin/node
const arr = process.argv.slice(2).map(Number);
if (arr.length < 3) {
  console.log(1);
} else {
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
