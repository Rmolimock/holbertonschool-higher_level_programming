#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ArgvNum = 0; ArgvNum < this.height; ArgvNum++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
