class Vehicle:
    def __init__(self, brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
       
    def describeVehicle(self):
        print(f"{self.brand} {self.model} runs on {self.fuel_type}.")

class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass
first_vehicle = Car("Lamborghini","Hurracan","Gasoline")
first_vehicle.describeVehicle()
Second_vehicle= Motorcycle("Kawasaki","V2","Gasoline")
Second_vehicle.describeVehicle()
