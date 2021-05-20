

class Car:

    total_cars = 0
     # default will start from the right, here our default milage is 0
    def __init__(self, make: str, model: str, year: int, owner: str, milage: int = 0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner
        self.milage = milage
        Car.total_cars += 1

    def __str__(self) -> str:
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Owner: {self.owner}, Mile: {self.milage}"

    def drive_car(self, distance: int):
        print(f"Drive the car {distance} miles")
        self.milage += distance
    #class method. A method that is attached to the class
    # it does not pass in self as the arguent because it does not a class isntance
    # it is like a static method in Java
    def miles_to_kilos(miles: int):
        kilos = miles *1.6
        return kilos
    # objects are mutable and you can always add an attribute
    def paint_car(self, color: str):
        self.color = color
    
        


crosstrack = Car("Subru", "crosstrack", 2018, " Asif Mohammad")
crosstrack = Car("ubru", "crosstrack", 2014, " Asif Mohammad")
print(crosstrack)
crosstrack.drive_car(100)
print(crosstrack)
crosstrack.drive_car(50)
print(crosstrack)

kilometers = Car.miles_to_kilos(50)
print(kilometers)
#crosstrack.miles_to_kilos()
#crosstrack.paint_car("blue")
#print(crosstrack.color)
print( crosstrack.total_cars)







    