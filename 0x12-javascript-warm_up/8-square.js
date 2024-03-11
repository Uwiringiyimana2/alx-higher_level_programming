#!/usr/bin/node
const i = process.argv[2];
if (!isNaN(parseInt(i))) {
  const size = parseInt(i);
  for (let n = 0; n < size; n++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
