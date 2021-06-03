// functions are objects
// you can pass them arount your protram like strings or antything else
// functions can bew passed to another function as arg

const hello = () => {
    console.log("Hello");
}
hello();

cosnt x = hello();

x() //invoke the same function object in the variablel

function holla() {
    console.log("Holla");
}

function doTwice(func) {
    func()
    func()
}

doTwice(hello); // not invoking the hello objcet at line 19 // i am passionate in the object funciton
doTwice(holl);

// really common in js to pass in anonymous callback function

doTwice(()=>{ console.log("bonjore") }); // anonymous function
// callback function is the function PASSED in to the function
// higher order function is the function that accepts the funciton as an argument

// Python has terrible anonymous function
/** def do_twice(func): print(func(10)) print(func(10))
 * do_twice(lambda x: x+10, 100)
 */

