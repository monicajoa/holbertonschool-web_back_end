export default class Airport {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
