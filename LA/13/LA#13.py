class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        self.can_swim = True

Fish1 = Fish("Salmon","salmon",True)
print(Fish1.can_swim)
