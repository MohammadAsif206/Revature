def say_hello():
   print("Hello")
def hola():
    print("Holla")

def num_twice(func):
    def inner():
        func()
        func()
    return inner

d_hello = num_twice(say_hello)


# bc this is such a helpful trick many programming lanugat have easy syntax

@num_twice
def bonjur():
    print("Banjour")
bonjur()

@dataclass # in built decorator that reads you class field in a class
# turns then into instance var , create a default construcotr and default __init__
class Person:
    name: str
    age: int
    profession: str
adam = Person("Adam", 12, "Trainer")

print(adam.__dict__)
