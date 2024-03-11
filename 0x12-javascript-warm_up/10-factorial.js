#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num <= 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (!isNaN(num)) {
  console.log(factorial(num));
} else {
  console.log(1);
}
