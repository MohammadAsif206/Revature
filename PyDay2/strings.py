#String are one of the most common data types in any programming languages

# Sstring literal is just defining  a stirng as uch

name = " Adam"

#Stein interpolation putting variables into string

greeting = "Hello "+ name + " it is great to meet you!"

# f is format interplate valude into your string using {}
greeting = f"Hello {name} it is awesome to see you! {7<8}"

greeting = "Hello {person} is great to see you! Alas something else {phrase}".format(person='Alice', phrase='hi')

print(greeting)

# string slicing is being able to tatke substring out of a larger string

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# start at 0 go the 4th character. that is exclusive
abc = alphabet[0:3]
jk = alphabet[9:11]

#negative index
print(alphabet[len(alphabet)- 1])
#-1 is the last element -2 second to last etc. this is the best the above one is not good
print(alphabet[-1])
# the last argument is the step
everyother = alphabet[0:14:2]
#you can do it in reverse also
zyx = alphabet[::-1]
print(zyx)

#delete a character
l = list(alphabet) # this generates a brand new list
del l[2]
print("".join(l))

# you can make anything a string by using the str function
x = 100
y = str(x)
print(type(y))

#strigs are immutable, cannot be altered once created
# Note everything is an object on Python
phrase = " hello everyone"
phrase[8] = "A" # throws an error because strings are immutable CANNOT be altered once created