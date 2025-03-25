const express = require('express');
const app = express()
const port = 7865


app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system')
});


if (require.main === module) {
  const PORT = 7865;
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}


module.exports = app;
