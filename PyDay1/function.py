# function is a reusable chunk of code, they can have parameters where you pass in arguments

#def for define
# void functions do not return anything, if you do not return anything it returns None
# highly recommend for functions do type annotation

def hello():
    print("This is a simple funciton")
    print("it just says Hello")
def greet_person(name):
    print("Hello " + name)
hello()
greet_person("Mohammad")

# I highly recommend using type annotation for your functions
def greater_number(num1:float, num2: float) -> float:
    if num1 > num2:
        return num1
    else:
        return num2
i = greater_number(90.1, 45.4)
print(i)

# take in 
def num_caps(phrase: str) -> int:
    pass # allows the code compile showing this function is not implemented yet
    counter = 0
    for c in phrase:
       if c.isupper():
           counter += 1
    return counter
ups = num_caps("sldnDALCAlCATAC")
print(ups)

# in python you can pass argument in posionally like, java or js
def multi_print(phrase: str, times: int) -> None:
    for i in range(times):
        print(phrase)
multi_print("Hello Everyone", 10)
#f you can pass funciton using the named variables
# the below two lines of codes are identical
multi_print(times=10, phrase="Hello Everyone")
multi_print(phrase="Hello Everyone", times=10)