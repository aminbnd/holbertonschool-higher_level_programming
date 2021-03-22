#!/usr/bin/node

function factorial (n) {
  let result = 1;
  for (let i = n; i >= 1; i--) {
    result = result * i;
  }
  return result;
}
console.log(factorial(parseInt(process.argv[2])));
