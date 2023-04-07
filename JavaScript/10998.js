let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");
let line = input[0].split(" "); // 맨 첫 줄
let a = parseInt(line[0]);
let b = parseInt(line[1]);
console.log(a * b);
