const uc = require("upper-case");

if (process.argv.length > 1) {
    console.log(uc(process.argv[2]));
}
