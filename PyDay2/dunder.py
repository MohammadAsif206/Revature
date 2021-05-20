class String:
    def __init__(self, greeting: str) -> None:
        self.greeting = greeting
        
    # a method to print the string1
    def __repr__(self) -> str:
        return 'Object: {}'.format(self.greeting )

    # to allow concatination
    def __add__(self, other):
        return self.greeting + other


# Drive code
if __name__ == __name__:
    #object creation
    string1 = String('Hello')

    # print object location
    print(string1 + " Mohammad")