const calculateNumber = require("./2-calcul_chai");
const expect = require('chai').expect;

describe("calculateNumber", function() {
  it("When type is SUM, round the two numbers, and add a from b", function() {
    const result = calculateNumber('SUM', 1.4, 4.5);
    expect(result).to.equal(6);
  });

  it("When type is SUM, round the two numbers, and add a from b", function() {
    const result = calculateNumber('SUM', 1.4, 0);
    expect(result).to.equal(1);
  });

  it("When type is SUBTRACT, round the two numbers, and subtract b from a", function() {
    const result = calculateNumber('SUBTRACT', 1.4, 4.5);
    expect(result).to.equal(-4);
  });

  it("When type is SUBTRACT, round the two numbers, and subtract b from a", function() {
    const result = calculateNumber('SUBTRACT', 0, 4.5);
    expect(result).to.equal(-5);
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    const result = calculateNumber('DIVIDE', 1.4, 4.5);
    expect(result).to.equal(0.2);
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    const result = calculateNumber('DIVIDE', 0, 4.5);
    expect(result).to.equal(0);
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    const result = calculateNumber('DIVIDE', 1.4, 0);
    expect(result).to.equal('Error');
  });

  it("When type is DIVIDE, round the two numbers, and divide a with b - if the rounded value of b is equal to 0, return the string Error", function() {
    const result = calculateNumber('DIVIDE', 1.4, 0.2);
    expect(result).to.equal('Error');
  });
});
