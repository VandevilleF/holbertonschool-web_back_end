const expect = require('chai').expect;
const request = require('request');
const app = require('./api');

const server = app.listen(7865, () => console.log('Test server running on port 7865'));
const url = 'http://localhost:7865';

describe('GET /', () => {
  it('respond with the message Welcome to the payment system', function (done) {
    request.get(`${url}/`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('GET /cart/:id', () => {
  it('return Payment methods for cart :id', function (done) {
    request.get(`${url}/cart/12`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('return 404 when id is not a number', function (done) {
    request.get(`${url}/cart/hello`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

// Arrêter le serveur après les tests
after(() => {
  server.close();
});
