const {Server} = require('ws');
let wsserver = new Server({ port: 8080, path: '/' });
let latest = //TODO: figure out whether userid needs handling here
    { time: Date.now(), msg: "no messages yet" };

 wsserver.on('connection', ws => {
    console.log("New client connected");
    ws.send(JSON.stringify(latest)+"\n");
    ws.on('close', (code, msg) => console.log("Connection closing", code, msg));
    ws.on('message', msg => {
        //TODO: figure out whether userid needs handling here
        latest = { time: Date.now(), msg: msg };
        console.log("Message arrived", msg);
        wsserver.clients.forEach(c => c.send(JSON.stringify(latest)));
    });
});