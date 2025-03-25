const expect = require('chai').expect;
const request = require('request');
const app = require('./api');

let server;
const baseURL = 'http://localhost:7865';

describe('API GET /', () => {
  before(function (done) {
    server = app.listen(7865, done);
  });

  after(function (done) {
    server.close(done);
  });

  it('respond with the message Welcome to the payment system', function (done) {
    request.get(`${baseURL}/`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    })
  });

  it('respond with the message Welcome to the payment system', function (done) {
    request.get(`${baseURL}/`, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    })
  });
  it('responds with 200 for a valid cart ID', function (done) {
    request.get(`${baseURL}/cart/12`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('responds with 200 for a valid cart ID', function (done) {
    request.get(`${baseURL}/cart/12`, (err, res, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('responds with 404 for an invalid cart ID not an number', function (done) {
    request.get(`${baseURL}/cart/hello`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

