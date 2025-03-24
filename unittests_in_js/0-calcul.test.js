import { calculateNumber } from "./0-calcul.js";
import assert from 'assert';

describe("calculateNumber", function() {
  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1, 3), 4);
  });
});
describe("calculateNumber", function() {
  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
});
describe("calculateNumber", function() {
  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
});
describe("calculateNumber", function() {
  it("Round a and b and return the sum of it", function() {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
});
