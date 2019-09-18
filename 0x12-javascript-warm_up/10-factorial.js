#!/usr/bin/node
function factorial (a) {
  a = Number(a);
  if (isNaN(a * (a - 1))) {
    return (1);
  } else if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

console.log(factorial(process.argv[2]));
