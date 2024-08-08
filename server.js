const express = require('express');
const cors = require('cors');  
const app = express();  

app.use(cors());  

const port = 7000;

app.get('/add/:num1/:num2', (req, res) => {
  const num1 = parseFloat(req.params.num1);
  const num2 = parseFloat(req.params.num2);
  const sum = num1 + num2;
  res.send(`${sum}`);
});

app.get('/subtract/:num1/:num2', (req, res) => {
  const num1 = parseFloat(req.params.num1);
  const num2 = parseFloat(req.params.num2);
  const difference = num1 - num2;
  res.send(`${difference}`);
});

app.get('/multiply/:num1/:num2', (req, res) => {
  const num1 = parseFloat(req.params.num1);
  const num2 = parseFloat(req.params.num2);
  const product = num1 * num2;
  res.send(`${product}`);
});

app.get('/divide/:num1/:num2', (req, res) => {
  const num1 = parseFloat(req.params.num1);
  const num2 = parseFloat(req.params.num2);
  if (num2 !== 0) {
    const quotient = num1 / num2;
    res.send(`${quotient}`);
  } else {
    res.status(400).send('Cannot divide by zero.');
  }
});

app.get('/factorial/:num', (req, res) => {
  const num = parseInt(req.params.num, 10);
  if (num < 0) {
    res.status(400).send('Factorial of a negative number is undefined.');
  } else {
    let factorial = 1;
    for (let i = 2; i <= num; i++) {
      factorial *= i;
    }
    res.send(`${factorial}`);
  }
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});