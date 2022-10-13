const http = require('http');

let score = { home: 1, away: 0 };

let server = http.createServer((req,res) => {
    res.writeHead(200, {"Content-Type": "text/json",
                        "Access-Control-Allow-Origin": "*"});
    res.end(JSON.stringify(score)+"\n");
})
server.listen(8080);

function printscore() {
    console.clear();
    console.log("Welcome to the football live score UI and webserver!");
    console.log("Send an HTTP request to localhost:8080 for live score.");
    console.log("Press h for home team goal, 'a' for away team goal, and Ctrl-C or 'q' to exit");
    console.log("");
    console.log("home: " + score.home + " away: " + score.away);
}

process.stdin.setRawMode( true ); // enable char-by-char input
printscore();
process.stdin.on('data', buf => {
    switch (buf.toString()) {
    case '\u0003': // unicode char for Ctrl-C
    case 'q': 
        process.exit(0);
    case 'h':
        score.home++;
        printscore();
        break;
    case 'a':
        score.away++;
        printscore();
        break;
    default:
        printscore();
        console.log("input not understood: ", buf.toString());
        break;
    }
});
