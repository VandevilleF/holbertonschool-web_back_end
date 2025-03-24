const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token')

describe("getPaymentTokenFromAPI", function () {
  it("should get the result of getPaymentTokenFromAPI", function (done) {
    getPaymentTokenFromAPI(true)
    .then((response) => {
      expect(response).to.deep.equal({ data: 'Successful response from the API' });
      done();
    })
  });
});
