function calculateNumber(type, a, b) {
  switch(type) {
    case 'SUM':
      return Math.round(a) + Math.round(b);
    case 'SUBTRACT':
      return Math.round(a) - Math.round(b);
    case 'DIVIDE':
      if (b != 0) {
        return Math.round(a) / Math.round(b);
      }
      return ("Error")
  }
}

module.exports = calculateNumber;
