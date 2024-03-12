#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      this.width;
      this.height;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
