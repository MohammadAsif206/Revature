// arrays are very similiar to arrays in py
// you can define them using array literal syntax
// they dynamically resize, and can contain anything

let nums = [1, 5, 0, 6];
let stuf = [" asif", null, 9, "g", ["asi", " do", 9]];
for (const num of stuf) {
    console.log(num); // iterate over an array

}

stuf[3] // retrieves 4th element from the array

nums.map(nums)