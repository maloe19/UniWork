const {Server} = require('ws');
let wsserver = new Server({ port: 8080, path: '/' });

let latest = { time: Date.now(), msg: "no messages yet" };

wsserver.on('connection', ws => {
    ws.send(JSON.stringify(latest)+"\n");
    ws.on('close', (code, msg) => console.log("Connection closing", code, msg));
});

process.stdin.on('data', data => {
    latest = { time: Date.now(), msg: data.toString() };
    process.stdout.write("new input message at " + latest.time
                         + ": " + latest.msg);
    wsserver.clients.forEach(c => c.send(JSON.stringify(latest)));
});
