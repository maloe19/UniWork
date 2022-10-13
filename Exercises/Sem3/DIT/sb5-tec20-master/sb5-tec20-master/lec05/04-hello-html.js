const http = require('http');

let server = http.createServer((request, response) => {
    console.log("getting a request");
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write("<!DOCTYPE html>");
    response.write("<html>");
    response.write("<head></head>");
    response.write("<body>");
    response.write("  <p>Hello World!</p>");
    response.write("</body>");
    response.end("</html>");
});
server.listen(8080);