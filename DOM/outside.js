// function external() {
//     alert("External JS");
// }

let calc = function(num1, num2, calcType) {
    if (calcType === "add") {
        return num1 + num2;
    } else if (calcType === "multiply") {
        return num2 * num1;
    } else {

        return num1 / num2;
    }
}
console.log(calc(4, 5, "multiply"));