// JS for a LONG time did not have classes
// Objects literal were the primary way to create objects. Stil are
// object in JS is just a collection of key value pairs
//similiar to py dic
// there are no restrection to what the values in an object are

adam = {
        name: "Adam",
        age: 19,
        profession: "Trainer",
        language: ["Java", " JavaScript", " C++"],
        sayHello: function() {
            // this is very similiar to the self keyword in py
            console.log("hello my name is: " + this.name); // will use the name on the object
        }

    }
    // you crated an object NOT based on a class
console.log(adam);
console.log(adam.name);
//JSON javaScript Object Notation
//browsers haqve in built support for turning JSON and vice versa

const json = JSON.stringify(adam) // objects to JSON strin
console.log(json);
const player = '{"name": "Asif", "position": "pg"}'
const playerObj = JSON.parse(player)
console.log(playerObj)
adam.sayHello();

// js did not have classes so it did not classical inherritence
// js has protocol inheritence . one objec points to another object and copies its properties

const mike = { name: "Mike" }; // brand new object
mike.__proto__ = adam // mike will inherit the properties
console.log(mike);
mike.sayHello(); // it inherit the function. the this keyword for the mine object

// the differene between the ()=> and function(){} is the this keyword
// function the this keyword is dynamic . the this can change
// ()=> the this keyword only applies to a single object

employee1 = {
    title: "SN",
    description: function() {
        console.log(this.title);
    }
}
employee2 = {
    title: "JN",
    description: function() {
        console.log(this.title);
    }
}
employee2.__proto__ = employee1;
employee2.description();
const func = employee1.description();

class Person {
    static counter = 0;
    constructor(name, age) {
        this.name = name;
        this.age = age;
        Person.counter += 1;
    }
    sayHello() {
        console.log("Hello my name is: " + this.name);
    }

}
const hank = new Person("Hank Hill", 40);
console.log(hank);