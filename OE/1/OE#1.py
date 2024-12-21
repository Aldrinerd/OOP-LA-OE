class Hero:
    def __init__(self, hero_name, role, damage_type):
        self.hero_name = hero_name
        self.role = role
        self.damage_type = damage_type
    def describe(self):
        print(f"{self.hero_name} is a {self.role} hero and deals {self.damage_type} damage")
    def __str__(self):  
        return f"{self.hero_name}, {self.role}, {self.damage_type}"
hero1 = Hero("Granger","marksman","physical")
hero2 = Hero("Fanny","assasin","physical")
hero3 = Hero("Tigreal","tank","physical")
hero4 = Hero("Harith","mage","magic")
hero5 = Hero("Alucard","fighter","physical")
#test
hero1.describe()
hero2.describe()
hero3.describe()
hero4.describe()
hero5.describe()
