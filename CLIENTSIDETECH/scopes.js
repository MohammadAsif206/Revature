// JS does not have the same scoping as PY
// JS scopes are defined via Kywords rather than location

function hello() {
    var name = " Asif"; // var makes the variable Function scope
    console.log(name);
}
hello();

console.log(name)

function hola() {
    console.log(nomber);
    var nomber = "James"; // hoisting is 'feature of JS'
    // BEFORE a function exectutes the var var in it are given the val of undefined
    console.log(nomber);
}
hola();

// let and const keywords, they are used to make variables BLOCK scoped
// cannot be hoisted

function bnojore() {
    let name = "Jaxson";
    // name is only in the scope of the curly bracket
    console.log("bonf" + name);
}
bnojore();
// use let and const . Never use var
// avoid global variables whenver possible
let x = 100;
x = 90;
// constant variables cannot be changed once assigned
// have the same scoping rules as let
const y = 1000;

y = 900;