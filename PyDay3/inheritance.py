# Inheritance in py
# inheritance is the ability o fon class to recieve attributes from another class
# attributes are instance variables self. something and the method def m(self)
# PY DOES have multiple inheritance (It is very rare to actually have to use it)

class Employee:

    def __init__(self, e_id: int, f_name: str, l_name: str) -> None:
        self.e_id = e_id
        self.f_name = f_name
        self.l_name = l_name
    
    def __str__(self) -> str:
        return f"the employee is {self.f_name} {self.l_name}"

steven = Employee(101, "steve", "kil")
print(steven)

# you pass in the parent class Trainer inherits Employee
class Trainer(Employee):
    def __init__(self, e_id: int, f_name: str, l_name: str, favorite_language: str) -> None:
        print("In trainer constructor")
        super().__init__(e_id, f_name, l_name) # in PY
        # explicitly create your Parent user the parent init dunder method
        self.favorite_language = favorite_language
    def __str__(self) -> str:
        return f"Trainer is {self.f_name} {self.l_name} and favorite language is {self.favorite_language}"

adam = Trainer(202, "Adam", "Kelsy", " TypeScript")
print(adam)

# Duck typing if it looks like a duck and quacks like a duck is a duck
#duck.quack() and it give you the output you want you might as well treat it like