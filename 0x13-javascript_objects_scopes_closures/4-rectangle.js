#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.create(null);
    }
  }

  // method that prints
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // method that exchanges with and height
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // method that multiplies with and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
