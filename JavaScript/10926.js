let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let line = input[0].split(" ");
let id = toString(line[0]);
console.log(id + "??!");
