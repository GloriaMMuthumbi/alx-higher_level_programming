#!/usr/bin/node

function add (num1, num2) {
  return (num1 + num2);
}

const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
