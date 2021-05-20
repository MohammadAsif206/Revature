# Pthon has your typical if else while for as most programming language
x = 100
#python does not use curly brackets, it used colons, new lines and indenting to create blocks of codes
if x < 10 :
    print('the value is less than ')
elif x == 10: # elif is a combination of else if
    print("the value is 10")
else:
    print("the vlaue us 10 or greater")

i = 0
while( i < 100):
    if i% 2 == 0:
       print("even " + str(i))
    else:
        print("odd" + str(i))
    i = i+1
    # identical to i += 1. there are no i++ in python

