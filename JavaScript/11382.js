let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let line = input[0].split(" ");

const a = parseInt(line[0]);
const b = parseInt(line[1]);
const c = parseInt(line[2]);

console.log(a + b + c);
