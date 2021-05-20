# dictionaries
# dat structure that store things as key value pairs
# dictionaries do not allow duplicate keys
#you can add or remove key values from a dictionary or edit the values inside of it
# if we have duplicate keys one will be overwridden

def welcome():
    print("Welcome")

emails = {
    "Adam":{"phone_number":"333-333-5555","email": "adam.ranier@revature.net"},
     "Richard":"rechard.22@hotmail.com",
     "siera": "hker@gmail.com",
     965: "Hello World", # you can have any types of key
     None: 1000,
     "funct": welcome
     }

print(emails["Adam"])
print(emails.get("Aaa", "Default"))
print(emails)