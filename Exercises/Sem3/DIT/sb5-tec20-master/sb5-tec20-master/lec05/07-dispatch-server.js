// Originally from 
// http://blog.modulus.io/build-your-first-http-server-in-nodejs

const http = require('http');

let dispatch = Object.create(null);
// handlers
dispatch.GET = (request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end("Thanks for the GET request\n");
}
/*
dispatch.PUT = (request, response) => {   
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end("Thanks for the PUT request\n");
}
*/
dispatch.POST = (request, response) => {
    request.on('data', data => console.log(''+data));
    request.on('end', () => {
        response.writeHead(200, {'Content-Type': 'text/plain'});
        response.end("Thanks for the POST request\n");
    });
}
/*
dispatch.DELETE = (request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end("Thanks for the DELETE request\n");
}

dispatch.OPTIONS = (request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end(null);
}
*/
let server = http.createServer((request, response) => {
    console.log(request.method, request.url);
    try { dispatch[request.method](request, response); }
    catch (err) {
        response.writeHead(405, {'Content-Type': 'text/plain'});
        response.end('Method not allowed\n');
    }
});
server.listen(8080);
console.log("Listening to http://localhost:8080");
