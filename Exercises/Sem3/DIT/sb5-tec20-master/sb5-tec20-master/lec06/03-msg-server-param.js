// query with, e.g., curl http://localhost:8080?time=1538994691532

const http = require('http');
const url = require('url');

let latest = { time: Date.now(), msg: "no messages yet"}

function writeResponse(res, content) {
    res.writeHead(200, {"Content-Type": "text/json",
                        "Access-Control-Allow-Origin": "*"});
    res.end(content);
}

let server = http.createServer((req,res) => {
    let urlobj = url.parse(req.url, true);
    if (latest.time > urlobj.query.time) {
        writeResponse(res, JSON.stringify(latest)+"\n");
    } else {    
        writeResponse(res, JSON.stringify({})+"\n");
    }});
server.listen(8080);

process.stdin.on('data', data => {
    latest = { time: Date.now(), msg: data.toString() };
    process.stdout.write("new message at " + latest.time
                         + ": " + latest.msg)});