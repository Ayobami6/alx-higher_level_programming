#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // eslint-disable-next-line lines-between-class-members
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  // eslint-disable-next-line lines-between-class-members
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
  // eslint-disable-next-line lines-between-class-members
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
