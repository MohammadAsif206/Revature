# py common data structures
# data structures are just ways for us to store info for easy acce4ss and use

names = ["Adam", " Bill", "Steve"]

# lists will resize as needed and can store any types
# lists are mutable, you can always add or remove elements whenever you want
# lists can contains duplicate elements
#

stuff = ["apple", 4, [ ], 4, 4, None , None, 9.0]
print(stuff)

# to define a list 
my_list = []
#append always add an item towards the end of the lis but with insert we can add element in a specific desired location
my_list.append("Hello")
my_list.append("World")
my_list.insert(1, " !")

print(my_list)
#delete an item
del my_list[1]
my_list.extend(stuff)
# this a better way of doing the line abobe
print(my_list)

stuff[2].append("Added for inner list")
print(stuff)

# we can us is keyword to check if two objects are the same
stuff1 = stuff
print(stuff1 is stuff)

# make a shallow copy of the list
my_list.copy()




