# a simple greeting app that supports saying hello in many different languages
import english # import the py file ( a py file is called a module)
from spanish import hola # this is enforced in this course, if not stick to it, just be consistent
from germanic.germany import guten # this is imported from a nested folder
name = "Adam"

english.hello(name) # if you import just the module you have to use the module name to access the global funciton and variables
#if you use from , you can specify what function you want in particular, do not prefix with the module name
hola(name)
guten(name)


# py is an interpreted language that is executed line by line
# most py interpreters ( the software that reads your code and executes it)
# will ( compile imported files into machine code native the computer)
# by default .pyc C implementation of your py code

# a py file is a module
# a folder that contains one or many py modules is called a package
# __init__.py file in a package Older version of py required  this exact file name 
# to be in a package otherwise it would not import the module correctly

# every module ( py file) has a built-in variable called __name__
# the value of that variable is the name of the module
#UNLESS you are running that module directly

# the __name__ value is "__main__" if it is the file you are DIRECTLY executing otherwise it is the name of the file
print(__name__)

#Essentailly python's way of creating an entrypoint, like main method that you might see in
# other programming languages
if __name__ =="__main__":
    print("I can only run if you directly execute this file")