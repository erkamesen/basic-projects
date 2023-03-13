// npm init - - - npm install
const superheroes = require("superheroes");
const supervillains = require("supervillains");

var mySupervillainsName = supervillains.random();
var mySuperheroName = superheroes.random();

console.log("I feel like " + mySuperheroName + "today !\nAlso a little bit "+ mySupervillainsName);