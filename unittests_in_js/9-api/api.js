const express = require('express');
const app = express();


app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system')
});

app.get('/cart/:id', (req, res) => {
  if (isNaN(req.params.id)) {
    return res.status(404).send('Cart not found');
  }
  res.status(200).send(`Payment methods for cart ${req.params.id}`);
})

if (require.main === module) {
  const PORT = 7865;
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}


module.exports = app;
