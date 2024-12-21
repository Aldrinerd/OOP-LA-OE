class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating!")
    def info(self):
        print(self.brand, self.model)
class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")
class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")
class Microwave(Appliance):
    def operate(self):
        print("Heating food!")
washingMachine = WashingMachine("Hanabishi", "3000")
refrigerator = Refrigerator("Samsung", "9000")
microwave = Microwave("LG", "1000")

for appliance in (washingMachine, refrigerator, microwave):
    appliance.operate()
    appliance.info()
