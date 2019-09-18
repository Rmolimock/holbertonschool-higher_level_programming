#!/usr/bin/node
if (!isNaN(Number(process.argv[2]))) {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    let array = [];
    for (let j = 0; j < Number(process.argv[2]); j++) {
      array.push('X');
    }
    console.log(array.join(''));
  }
} else {
  console.log('Missing size');
}
