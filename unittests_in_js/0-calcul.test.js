const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe("calculateNumber", function() {
  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1, 3), 4);
  });

  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1, 3.7), 5);
  });

  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });

  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });

  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1000.54, 450.1), 1451);
  });
});
