class Player:

    def __init__(self, health=30, attack=5, heal=3):
        self.health = health
        self.attack = attack
        self.heal = heal

    def attack(self):
        return self.attack

    def heal(self):
        return self.heal


class Enemy:

    def __init__(self, health=20, attack=5, heal=3):
        self.health = health
        self.attack = attack
        self.heal = heal

    def attack(self):
        return self.attack

    def heal(self):
        return self.heal