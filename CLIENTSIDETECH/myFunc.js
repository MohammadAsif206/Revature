// like every programming languag JS has function
// there are a few ways to define fucntions
// Good JS should have semicolon, JS will auto insert ; to it's best ability
// works 99% of the time and the other 1% will cost you hours of debugging

//fucntion keyword
function hello(name) {
    console.log("Hello " + name)
}
hello("Asif");

const hola = function(nomber) {
    console.log(" Hola " + nomber);
}
hola("Mohammad");

// arrow notation Does Not use the function keyword
// there are minor differences between functon and arrow notation
const salam = (nam) => {
    console.log("Nam: " + nam);
}
salam(" farsi name");

// functions in JS can be invoded iwth any nuber of arguments
// calling a funciton with too may few parameters will give the parameters
// a default value of undefined

function add(num1, num2) {
    return num1 + num2;
}
let sum = add();
console.log(sum);
sum = add(100);
console.log(sum);
sum = add(100, 100, 100); // any excess parameters are ignored
console.log(sum);

//js does not have type annotation but it default argument
// that can give your function intllisence and be a bit more robust

function bonjure(napel = "Jacque") {
    console.log(" Bonjor " + napel);
}
bnojore("Jacque");