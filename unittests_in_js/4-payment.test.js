const sinon = require("sinon");
const Utils = require('./utils');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./4-payment')



describe("sendPaymentRequestToApi", function () {
  it("should call Utils.calculateNumber with SUM, 100, 20", function () {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const spy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnce).to.be.true;

    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    expect(spy.calledWith('The total is: 10')).to.be.true;

    sinon.restore();
  });
});
