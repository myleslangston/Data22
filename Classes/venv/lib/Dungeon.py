
from random import randint


class Adventurer:
    def __init__(self, name, level=1, attack=5, health=10, mana=5, coins=0):
        self.name = name
        self.level = level
        self.attack = attack
        self.health = health
        self.mana = mana
        self.coins = coins

class Mage(Adventurer):
    def __init__(self, mana=10):
        self.mana = mana


class Warrior(Adventurer):
    def __init__(self, health=20):
        self.health = health


class Knight(Adventurer):
    def __init__(self, attack=10):
        self.attack = attack


class Enemy:
    def __init__(self, enemy_level_arg, health = 5, attack = 2):
        self.enemy_level_arg = enemy_level_arg
        self.health = health
        self.attack = attack

new_game_prompt = input("Would you like to start a new game? y or n? ")
if new_game_prompt == "y":
    player = Adventurer(input("And when tales are told of you, what name shall they sing praise of? "))
    player_level = player.level
    enemy_level = player_level + randint(1, 2)
    encounter_enemy = Enemy(enemy_level)
    encounter = input(f"You encounter a level {enemy_level} goblin. Will you fight or flee? ".format(encounter_enemy))
    if encounter == "flee":
        print("You bravely run away, making sure to grab a t-shirt emblazoned with the logo 'Battle Dungeon: Re-live the days of old!' on your way out.")
    elif encounter == "fight":
        encounter_enemy = Enemy(enemy_level)
        if enemy_level > 2:
            print(f"The goblin was too strong and impales you with your own blade. Better luck next time, mighty warrior {player.name}")
        else:
            print("You slay this mighty goblin and make your way to Fuffner-Figgle.")
            fuffner = input("Would you like to continue on this quest? y or n? ")
            if fuffner == "y":
                print("You enter the small village of Upper Fuffner-Figgle, famed for it's prize winning peach cheese. The township have clearly tired of the burden of guiding a seemingly endless queue of keen young adventurers waiting behind a small red rope at the boundary of the village. The nearby yokel posing like a bouncer to a city's most popular nightclub leers at you and ushers you in. They follow a well trodden path inundated with a number of crooked wooden signs accompanying it's full length. The path is met by the foot of a nearby rocky cliff face where a large red panelled door confronts you. You hand off the stub of your 'admit one' ticket and head inside.")
            else:
                print("Ruuuuun")
    else:
        input(f"You encounter a level {enemy_level} goblin. Will you fight or flee? ")
elif new_game_prompt == "n":
    pass
else:
    new_game_prompt = input("Would you like to start a new game? y or n? ")





