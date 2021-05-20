
# This console application allows you to add two number together
# exeptions and try excepts add resielency to your code
# if all inputs are correct and everything is how it is supposed to be (Happy path execution)
# exception are for when code does not follow happy path exectution
print("Awsome adding app")
in1 = input("Enter you first number ")
in2 = input("Enter you second number ")

try:
    num1 = float(in1)
    num2 = float(in2)
    sum = num1+num2

    print("The sum is {}".format(sum))
except ValueError:
    print("That was an invalid number:")
finally:
    print("I print at the end ")



