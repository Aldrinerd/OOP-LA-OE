import random #just added so that the monster attacks a random enemy
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacked {target.name}. {target.name}'s remaining health: {target.health}")
    def special_move(self):
        pass
    def defend(self, damage):
        self.health -= damage - 10
class Warrior(Character):
    def special_move(self):
        print("Warrior uses Shield Bash!")
        self.power *= 2
class Mage(Character):
    def special_move(self, target):
        print("Mage casts Fireball!")
        target.health -= 100
class Archer(Character):
    def special_move(self, target):
        print("Archer shoots a Piercing Arrow!")
        target.health -= 100
class Monster(Character):
    def special_move(self):
        self.health += 50
        print("Monster roars and gains extra health! remaining health:", self.health)
warrior = Warrior("Warrior", 100, 20)
mage = Mage("Mage", 80, 30)
archer = Archer("Archer", 90, 25)
monster = Monster("Monster", 1000, 20)
characters = (warrior, mage, archer, monster)
for character in characters:
    if character != monster:
        character.attack(monster)
        if character == warrior:
            character.special_move()
        else: character.special_move(monster)
    else:
        character.attack(random.choice(characters[:3]))
        character.special_move()
