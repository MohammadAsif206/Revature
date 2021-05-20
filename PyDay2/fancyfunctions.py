
# py is a dynamic lan that does not support function overloading
#this is a problem for developers bc rnameing essentially the same function for all the types
#parameters would be a mess

def say_hello():
    print("Hello Person")

def say_hello(name: str): # this line will Replace the funnction without argument
    print(f"Hello {name}")

#
def hola(name: str = None):
    if name is None:
        print("holla random person")
    else:
        print(f"Holla {name}")

def greet_many(*names): # vr args essentially a tuple
    print(names)
    for n in names:
        print("Hello "+ n)


#say_hello()
hola()
hola("Adam")
greet_many("Asif", "Khadija", " ali")

def super_greet(**kwargs): #key word arguments essentially made your arguments a dictionary
    print(kwargs)

super_greet(adam="Adam Binair", richard = "Richard Orr", siera = "Seir Nincol")

# kwargs are really popular for configuration function
# creating a connection to a database

def connect_to_database(**kwargs):
    username = kwargs[" username"]
    password = kwargs["2333"]
    print(username)
    print(password)
#connect_to_database(username="adamgator", password="123ff")

#credentials = {"username":"adamgator", "password":"123ff"}
#connect_to_database(**credentials)

