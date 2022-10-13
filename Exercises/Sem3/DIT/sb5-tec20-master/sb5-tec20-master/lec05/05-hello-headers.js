const http = require("http");
let server = http.createServer((request, response) => {
    console.log('HTTP version:', request.httpVersion);
    console.log('url:', request.url);
    console.log('method:', request.method);
    console.log('header:', request.headers);
    console.log();
    
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.end('Thanks for the headers\n');
});
server.listen(8080);
