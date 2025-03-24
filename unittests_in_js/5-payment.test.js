const sinon = require("sinon");
const Utils = require('./utils');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment')



describe("sendPaymentRequestToApi", function () {
  let spy;

  beforeEach(function () {
    // Before test, spy is set on console.log
    spy = sinon.spy(console, "log");
  });

  afterEach(function() {
    // After test, spy is on console.log clear
    sinon.restore();
  })

  it("should call Utils.calculateNumber with SUM, 100, 20", function () {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 120')).to.be.true;
  });

  it("should call Utils.calculateNumber with SUM, 10, 10", function () {
    sendPaymentRequestToApi(10, 10);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 20')).to.be.true;
  });
});
