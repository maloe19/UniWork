const http = require('http');

let latest = { time: Date.now(), msg: "no messages yet"};

let server = http.createServer((req,res) => {
    res.writeHead(200, {"Content-Type": "text/json",
                        "Access-Control-Allow-Origin": "*"});
    res.end(JSON.stringify(latest)+"\n");
})
server.listen(8080);

process.stdin.on('data', data => {
    latest = { time: Date.now(), msg:  data.toString() };
    process.stdout.write("new message at " + latest.time
                         + ": " + latest.msg)});