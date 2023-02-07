##Jimmy Correa
#classes.py
##Accepts input for car and stores into classes


##creating Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = input("Vehicle type: ")

##Creating autombile class
class Automobile(Vehicle):
    def __init__(self, vehicle_type):
        self.year = input("Year: ")
        self.make = input("Make: ")
        self.model = input("Model: ")
        self.doors = input("Doors: ")
        self.roof = input("Roof: ")
  
  ##Display vehicle method that display what is required in menu form      
    def displayVehicle(self):
        print("Vehicle type: ", self.vehicle_type)
        print("Year: ", self.year)
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Number of doors: ", self.doors)
        print("Type of roof: ", self.roof)

newVehicle = Automobile("Car")
newVehicle.displayVehicle()
    
