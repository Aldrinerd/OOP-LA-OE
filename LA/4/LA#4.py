class MLHero:
    def __init__(self, hero_name, role):
        self.hero_name = hero_name
        self.role = role
    def describe(self):
        print(f"{self.hero_name} is a {self.role} hero.")
    def __str__(self):
        return f"{self.hero_name} is a {self.role} hero."
    def printmethod(self): #method used to print the string representation based on LA#4's instructions
        print(self)
hero1 = MLHero("Layla","marksman")
hero1.printmethod()