# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
