# a lambda is an anonymous function
#() =?{}
# popular in funcitonal programming

def multiply_10(n):
    return n*10
num = [1,2,3,4,5,6]

result = map(lambda n : n*10, num)
for r in result:
    print(r)
# lambdas are Nowhere near as common or useful in py as in other languages like JS
