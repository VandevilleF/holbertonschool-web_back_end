export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  set size(size) {
    if (typeof size !== 'number') {
      throw new TypeError('size must be a number');
    }
    this._size = size;
  }

  set location(location) {
    if (typeof location !== 'string') {
      throw new TypeError('location must be a string');
    }
    this._location = location;
  }

  toString() {
    return this._location;
  }

  valueOf() {
    return this._size;
  }
}
