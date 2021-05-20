# in python everything is an object
# you can create your own objects by defining classes
# class names are in Camel Case

# funciton vs method
# function is named block of code that you can execute that is not attached to an object
#method is a named block of code that IS attached to an object
#if you 
import object101
class Person:
    #class variables are defined at the top of the class
    counter = 0
    # a constructor in python will create an instance of this class
    # a constructor MUST be named __init__(self)
    # in JAVA/JS you would define the instance variable at the top of the class
    #there is no overloading in python
    def __init__(self, name: str, age: int) -> None:
        #in Python variables are created and declared in the constructor using self in side the constructor
        # we don't need setter and getter in python
        # to make a var private, we can put double underscore __
        self.name = name
        self.age = age
        Person.counter += 1
    # any method in python for a class has self as the firs paramter
    def introduce_self(self):
        print(f"Hello my name is: {self.name} and am {self.age}")

    #dunder methods are special methods in py that begins and ends with double underscore __dunder__
    # you are encouraged as a developer to override  them for a class need

    # this is the dunder method called whenever you put str(obj)
    def __str__(self) -> str:

        return f"name: {self.name} , age: {self.age}"

    def __add__(self, other):
        return self.name + self.age + other
    
# name and age are instance variables
# there is of each variable PER person created
bland = Person("Asif", 44)
bland.name = "Asif"
bland.age = 45
print(bland.name)
print(bland.age)
bill = Person( "Bill", 55)
bill.name = " Bill"
bill.age = 34
print(bill.name)
print(bill.age)
# or we can do it
#asif = Person("Mohammad", 55)

#print(asif.name)
#print(asif.age)

#in most programming languages the instance is implicitly passed into method
# in python it must be explicitly
bill.introduce_self() # this is a alternate syntax to the below code
Person.introduce_self(bill)
# IDentical code
bland.introduce_self()

# a class variable is attached to the class itself and is accessed via the class name
print(Person.counter)

# Py is all about being as explicit as possible
# var with self. in front of them belogns to the objects created
# var with class name in front of them belongs to the class
a = str(bill)
b =  str(bland)
print(bill)
print(bland)

# __add__
print((bill.name + bill.age + " Hi"))