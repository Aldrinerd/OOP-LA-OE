from abc import ABC, abstractmethod
class Gamecharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
class Warrior(Gamecharacter):
    def attack(self):
        print("Swings sword!")
class Mage(Gamecharacter):
    def attack(self):
        print("Casts a fireball!")
class Archer(Gamecharacter):
    def attack(self):
        print("Shoots an arrow!")
class Healer(Gamecharacter):
    def attack(self):
        print("Casts healing spell on ally!")
warrior = Warrior()
mage = Mage()
archer = Archer()
healer = Healer()
for character in (warrior, mage, archer, healer):
    character.attack()
