#LEGB namespaces convention
# locla
#Enclosing
#Global
#Built-in
#when you define a variable the namespace basically determines where you can access it
#what variable you are referring to

# built-in in namespace the variables ant functions that are built-in the language, the highest level, where we do not define anything
#rint(id)

# global namespace is nny variable or function defined at the TOP-level of python
x = 100 # this is a global variable
# it can be used anywhere in this file or used in another file


#local variables are defined WITHIN a function or a code block

def say_hello():
    greeting = "Hellow Everyone" # greeting is local variable it is NOT global
    # you cannot get it in another file
    print(greeting)
say_hello()
#print(greeting) # you cannot call greeting here