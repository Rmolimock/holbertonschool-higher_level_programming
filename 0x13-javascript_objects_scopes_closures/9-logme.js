#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  function increase () {
    console.log(count + ': ' + item);
    count++;
  }
  increase();
};
