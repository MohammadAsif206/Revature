welcome = " Global welcome variable"

def greet():
    welcome = "local welcome variable"
    print(welcome) # LEGB to determine what this welcome variable refers to
    # the nearest namespace is the local one defined
name = "Globy mcGlobeFace"
# if python cannot find an enclosing one it will check the global namespace for a var named name
if True:
    name = "Ecnlosing Enclose"# if pyton cannot find local var named name it  see if
    # there is an enclosing one of that name
    if True:
        name = "Local McLocal"
        print(name)# python will look for a local variable named name
        #print(nonexistnet) # something that python cannot find
        # python
        #checked local: not found
        #checked enclosing: not found
        #checked global: not found
        #checked built-in: not found
        #name error
        
greet()
print(welcome)