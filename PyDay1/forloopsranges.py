
# in java for loop: (int i = 0; i<100; i++ ){ code}
#python uses ranges for a iterating a piece of code a fixed amount of times

#range(startnumber, targetnumber(exdlusive)), ten is not included; it will print from 0 to 9
#for i in range(0, 10):
    #print(i)
#the third parameter is how the steps ( how much to increment or decrement), it can have negative numbers also
for j in range(10, 0, -1):
    print(j)

for x in range(100, 1000, 3):
    print(x)

# you should not almost never be creating a range to iterate over a list
names = ["Adam", "Bob", "Alice", "Tim"]
for name in names: # iterate over list
    print(name)

# strings are iterable
hello = "Hello"
for c in hello:
    print(c)
#technically works but never do it
for i in range(0,len(hello)):
    print(hello[i])

# you can do it also, without having the first value
for n in range(12):
    print(n)

for c, i in enumerate(hello):
    if c == 1:
        print(c)
