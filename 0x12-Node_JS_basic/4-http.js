const http = require('http');

const app = http.createServer((resquest, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.end('Hello Holberton School!');
});

app.listen(1245);
module.exports = app;
