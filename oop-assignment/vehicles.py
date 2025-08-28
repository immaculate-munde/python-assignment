# vehicles.py

# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

# Car class
class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Boat is sailing 🚤")

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Polymorphism demonstration
vehicles = [my_car, my_plane, my_boat]
for v in vehicles:
    v.move()
