class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked and dealt {self.attack_power} damage. {target.name}'s remaining health: {target.health}")
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed themself by {amount}. Remaining health: {self.health}")
player1 = Player("Player1", 150, 50)
player2 = Player("Player2", 150, 30)
while True:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player1.name} won!")
        break
    player2.attack(player1)
    player2.heal(10)
    if player1.health <= 0:
        print(f"{player2.name} won!")
        break
