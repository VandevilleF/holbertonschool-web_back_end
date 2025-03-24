const calculateNumber = require("./1-calcul");
const assert = require('assert');

describe("calculateNumber", function() {
  it("When type is SUM, round the two numbers, and add a from b", function() {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it("When type is SUM, round the two numbers, and add a from b", function() {
    assert.equal(calculateNumber('SUM', 1.4, 0), 1);
  });

  it("When type is SUBTRACT, round the two numbers, and subtract b from a", function() {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });

  it("When type is SUBTRACT, round the two numbers, and subtract b from a", function() {
    assert.equal(calculateNumber('SUBTRACT', 0, 4.5), -5);
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    assert.equal(calculateNumber('DIVIDE', 0, 4.5), 0);
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
