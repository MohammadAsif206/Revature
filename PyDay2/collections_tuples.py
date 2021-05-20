
#typles are essentially immutable lists
# tuples can be of any size when created
#tuples can have duplicates
# tuples can have any types

# tuples are created much like lists except with parenthesis
ssbu_fighters = ("Peach", "Zelda", "Little Mac", "Samus")

#del ssbu_fighters[2]
print(ssbu_fighters[2])
# you cannot delete from tuples
# you cannot append to tuples
x = ssbu_fighters[0:2]
print(x)

# code to the principle of least privellages
# if the values do not need to be altered then do not make mutable