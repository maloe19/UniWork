const http = require("http");
const url = require("url");

let server = http.createServer((request, response) => {
    let urlobj = url.parse(request.url, true);
    
    console.log('pathname:', urlobj.pathname);
    //console.log('search:', urlobj.search);
    console.log('query:', urlobj.query);
    
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.end('Thanks for the request\n');
});
server.listen(8080);
console.log("Listening! (port 8080)");