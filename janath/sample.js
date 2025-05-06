// Import the HTTP module
const http = require('https');

// Define the hostname and port
const hostname = 'localhost';
const port = 9000;

// Create the server
const server = http.createServer((req, res) => {
  // Set the response HTTP status code to 200 (OK) and content type to plain text
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // Send the response body "Hello, World!"
  res.end('Hello, World!\n');
});

// Start the server and listen on the defined port and hostname
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
