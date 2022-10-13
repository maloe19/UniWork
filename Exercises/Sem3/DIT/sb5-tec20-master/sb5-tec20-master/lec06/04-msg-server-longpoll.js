const http = require('http');
const url = require('url');

let latest = { time: Date.now(), msg: "no messages yet"}
let waiting = []

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
        waiting.push(res);
        res.setTimeout(5000, () => {
            console.log("timed out");
            let index = waiting.findIndex(e => e == res);
            if (index !== -1) { //still waiting?
                console.log("sending {}");
                writeResponse(res, JSON.stringify({})+"\n");
                waiting.splice(index,1); 
            }
        });
    }});
server.listen(8080);

process.stdin.on('data', data => {
    latest = { time: Date.now(), msg: data.toString() };
    process.stdout.write("new message at " + latest.time
                         + ": " + latest.msg);
    waiting.forEach(res => {
        console.log("New msg arrived, notifying");
        writeResponse(res, JSON.stringify(latest)+"\n");
    });
    waiting = [];
});