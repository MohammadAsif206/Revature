// JS has Extremely aggressive type coercion
// JS will compare apple to orange even if they are both bananas

console.log(100 == 100) //true
console.log(100 == 100) // true js will coerce

// there are some inherent falsy values
// values taht coerce to false
console.log(Boolean("")); // false
onsole.log(Boolean(0)); // false
onsole.log(Boolean(null)); // false
onsole.log(Boolean(undefined)); // false
onsole.log(Boolean(NaN)); // false
// every other value in js will be True in a comparison
onsole.log(Boolean("0")); // true
onsole.log(Boolean("0" - 0)); // false
onsole.log(Boolean("100" - 0 + ("100" - 0))); // Js level 99999
// == loose equality operator
// you should not use. it will coerce values before checking eauality
// === strict equality will also check to see of same type

onsole.log(100 === "100"); // false
onsole.log(100 == "100"); // true

onsole.log(0 == "0"); // true
onsole.log(0 === ); // false