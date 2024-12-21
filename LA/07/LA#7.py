class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Lamborghini", "White")
car2 = Car("Porche", "White")

print(car1.brand, car1.color)
car1.color = "Yellow"
print(car1.brand, car1.color)
print(car2.brand,car2.color)
