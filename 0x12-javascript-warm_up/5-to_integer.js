#!/usr/bin/node
if (!isNaN(Number(process.argv[2]))) {
  console.log('My number: ' + Math.trunc(process.argv[2]));
} else {
  console.log('Not a number');
}
