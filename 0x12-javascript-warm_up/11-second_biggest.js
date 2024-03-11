#!/usr/bin/node

function isSecondBiggest(numbers) {
  const sortedNums = numbers.sort((a, b) => b - a);

  const uniqueNums = [...new Set(sortedNums)];

  if (uniqueNums.length < 2) {
    return (0);
  }

  return (uniqueNums[1]);
}

const args = process .argv.slice(2).map(Number);
console.log(isSecondBiggest(args));
