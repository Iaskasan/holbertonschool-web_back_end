const http = require('http');
const { exec } = require('child_process');
const url = require('url');

// run_countStudents.js
function runCountStudents() {
  const countStudents = require('./3-read_file_async');
  const path = process.argv[2];

  countStudents(path)
    .then(() => {
    })
    .catch((error) => {
      console.error(error.message);
    });
}

const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    const databasePath = process.argv[2];

    exec(, (error, stdout, stderr) => {
      if (error) {
        res.write(`Error: ${stderr}`);
      } else {
        res.write(stdout);
      }
      res.end();
    });
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
