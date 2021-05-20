# PY has errors and execptions. The exceptions usually have error in the name
# the only REAL error is a syntax error. Exceptions are all lOgic based

# why do programas have exceptions at all?
# if an error manages to avoid being caught by an except block all the way up the program
# your appliction will crash eventually

def celcius_to_farenheit(c):
    try:
        f = c*9/5 +32
        return f
    except TypeError: # this except blcok will only catch TypeErrors
        print("Input must be an int or float")
    except:
        print("Some other error must have occured")
    finally:
        print("This code WIL always execute if there is an error or not")
    

x = celcius_to_farenheit(100)
print(x)

# whenerver you write code that has a possibility of FAILIRE
# you can surrorund the code in a try: except block
# in the except clause you can OPTIONally put a type of error to check for
# putting nothing is a catch ALL
# the catch all blank except should ALWAYS go last
#ONLY ONe except block is executed when an error