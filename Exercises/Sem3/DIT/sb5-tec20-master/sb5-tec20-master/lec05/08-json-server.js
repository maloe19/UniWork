const http = require("http");
const url = require("url");

let db = [ { id: 0, name: "Jens Hansen" },
           { id: 1, name: "Hanne Jensen" },
           { id: 2, name: "Will Williamson"}
         ];

let dispatch = Object.create(null);
dispatch.GET = (request, response) => {
    switch (url.parse(request.url).pathname) {
        case "/users/0":
            response.writeHead(200, {"Content-Type": "text/json"});
            response.end(JSON.stringify(db[0]));
            break;
        case "/users/1":
            response.writeHead(200, {"Content-Type": "text/json"});
            response.end(JSON.stringify(db[1]));
            break;
        default:
            response.writeHead(404, {'Content-Type': 'text/plain'});
            response.end('Not found\n');
    }
}

http.createServer((request, response) => {
    console.log(request.method, request.url);
    try { dispatch[request.method](request, response); }
    catch (err) {
        response.writeHead(405, {'Content-Type': 'text/plain'});
        response.end('Method not allowed\n');
    }
}).listen(8080);
