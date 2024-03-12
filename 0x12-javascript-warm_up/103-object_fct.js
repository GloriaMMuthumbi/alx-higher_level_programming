#!/usr/bin/node
const myObj = {
  type: 'object',
  value: 12
};
console.log(myObj);
myObj.incr = () => {
  myObj.value += 1;
};
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
