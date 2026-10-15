const express = require('express');
const app = express();

app.get('/profile', (req, res) => {
  const userInput = req.query.name || 'guest';
  res.send('<html><body><h1>Hello ' + userInput + '</h1></body></html>');
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
