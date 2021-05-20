# We have been tasked with writing a short console app
# to see if a person's username is valid
# username has to be at least 6 characters long
# it must contain at least one number

# one is that the constructor is aleady set up take in message and display them
# two 
class InvalidUsernameErrror(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
    def __str__(self):
        return " gooffed"
def validate_username(username: str):
    if len(username)<6:
        raise ValueError(f"username must be at least 6 characters, it was {len(username)}")
    contains_number: bool = False
    for c in username:
        if c.isnumeric():
            contains_number = True
    if contains_number:
        return True
    else:
        raise ValueError("username must include at least one number")
# all errors in PY are runtime. There are no checked exceptions
# there is no way to know if a function raises an error untill you actually call it
validate_username("at1")