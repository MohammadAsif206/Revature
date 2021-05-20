# common Errors in PY
# LookupError: try to get an index from a list or tuple that does not exist or use dictionary key taht does not exist
# TypeError: when you pass in a variable that is of the wront type (pass in a string instead of an int )
#ValueError: when the type is right but the value of that variable is wrong
# NameError: you reference a variable that does not exist
#Often functions will raise errors and NOT handle them
# For functions that might be used throughout the program you can handle the errors differntly
# most appropriatley
# ... (three dots ) works the same as 'pass' used when showing not implemented and allows you to skip that part and come back later 
def celcius_to_farenheit(c):
    # Exceptions give you information on WHY something failed
    # Code can fail in multiples way and you might address them differently
    if type(c) != int and type(c) != float:
        raise TypeError("Temprature must be a numeric type")
    if c < -273:
        raise ValueError("Input Temp {c} is below absolute zero -273 C'")
    f = c*9/5 +32
    return f
try:
    result = celcius_to_farenheit(-666)
except TypeError as e:
    print(e)# prints out the message you passed when you created the Error
    # the __str__ for errors is to return the message it waws create with
except ValueError as e:
    print(e)
