export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand !== 'string') throw new TypeError('brand must be a string');
    if (typeof motor !== 'string') throw new TypeError('motor must be a string');
    if (typeof color !== 'string') throw new TypeError('color must be a string');

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter for brand
  get brand() {
    return this._brand;
  }

  // Getter for motor
  get motor() {
    return this._motor;
  }

  // Getter for color
  get color() {
    return this._color;
  }

  // Method to clone the car
  cloneCar() {
    return new Car(this._brand, this._motor, this._color);
  }
}
