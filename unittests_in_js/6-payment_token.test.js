const getPaymentTokenFromAPI = require('./6-payment_token')

describe("getPaymentTokenFromAPI", function () {
  it("should get the result of getPaymentTokenFromAPI", function (done) {
    getPaymentTokenFromAPI(true)
    .then(() => {
      done();
    })
  });
})
