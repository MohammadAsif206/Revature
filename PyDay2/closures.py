def outer(name):
    greeting = " how are your "+ name
    def inner():
        print(greeting)
    return inner

asif_greeter = outer("Asif")
bill_greeter = outer("Bill")
asif_greeter()
bill_greeter()

def is_palindrome(phrase: str):
    def reverse(word):
        return word[:: -1]
    if phrase == reverse(phrase):
        return True
    else:
        False
print("This is palindrem")
print(is_palindrome("racecar"))