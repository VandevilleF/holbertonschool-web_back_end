function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({data: 'Successful response from the API' })
  }
  return Promise.reject(new Error('fail'));
}

module.exports = getPaymentTokenFromAPI;
