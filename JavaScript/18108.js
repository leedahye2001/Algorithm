let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let line = input[0].split(" ");

let y = parseInt(line[0]);
let x = 543;
console.log(y - x);
