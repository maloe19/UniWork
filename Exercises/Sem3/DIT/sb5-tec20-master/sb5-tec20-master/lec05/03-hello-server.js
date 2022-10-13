const {createServer} = require('http');

let server = createServer((request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World!');
});
server.listen(8080);