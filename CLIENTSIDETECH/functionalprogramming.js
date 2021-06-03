// callback function can be really helpful to make code look succinct and clear
// Arrays are a very common and helpful place to see callback function
//
const nums = [10, 20, 30, -10, 40, 50, 60, -20];
// imperative approach. using a loop is an imperative paradigm of programmin

for (const num in nums) {
    console.log(num);
}

function print(something) {
    console.log(something)
}

// arrays have a lot of helpful higher order alreay on them
//nums.forEach((num) => { console(num) }); // does the same exact thing
// foreach element in the list pass it into the callback function
nums.forEach(print) // does the same thing

// map higher order function that takes in a single element and returns a value
// filter remove any element that returns false from the function

const tempf = [212, 300, 102, 32, 10, -20] // temp in far
function farToCel(f) {
    return (f - 32) * 5 / 9;
}

const tempC = tempf.map(farToCel); // this will return a new array with each element through that function
// let temp2 = [];
// for (let t of tempf){
//     temp2.push(farToCel(t))
// }
console.log(tempC);

function isPositive(num) {
    if (num >= 0) {
        return true;
    } else {
        return false;
    }
}

function roundNumber(num) {
    return Math.random(num);
}
const positiveF = tempf.map(isPositive);

console.log(positiveF);

// it can be realy easy to chain funcitons
// make an array of positvie celcius temp
const positiveC = tempf.map(farToCel).filter(isPositive).map(roundNumber);
console.log(positiveC);