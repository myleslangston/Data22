from random import randint


from smashclasses import *


print("Fight for your life against the Great Smashonator!")

player = Player()
enemy = Enemy()
turn = 0
gameover = 0

while gameover != 1:
    if player.health <= 0:
        print("You have been defeated by the Great Smashonator!!!")
        gameover = 1
    elif enemy.health <= 0:
        print("You have defeated the Great Smashonator!!!")
        gameover = 1
    else:
        if turn == 0 and player.health > 0:
            player_input = input("Would you like to attack or heal? ")
            while (player_input != "attack" or "heal") and turn == 0:
                if player_input == "attack":
                    resolved_attack = Player.attack(player)
                    enemy.health -= resolved_attack
                    print(
                        "You attack the Great Smashonator for {} HP! They have {} health left!".format(resolved_attack,
                                                                                                       enemy.health))
                    turn = 1
                elif player_input == "heal":
                    resolved_heal = Player.heal(player)
                    player.health += resolved_heal
                    print("You heal for {} HP! You have {} health left!".format(resolved_heal, player.health))
                    turn = 1
                else:
                    print("I'm sorry, I didn't understand your input! Please try again!")
                    player_input = input("Would you like to attack or heal? ")

        if turn == 1 and enemy.health > 0:
            ai_input = randint(1, 2)
            if ai_input == 1:
                resolved_attack = Enemy.attack(enemy)
                player.health -= resolved_attack
                print("The Great Smashonator smashes you for {} HP! You have {} health left!".format(resolved_attack,
                                                                                                     player.health))
                turn = 0
            elif ai_input == 2:
                resolved_heal = Enemy.heal(enemy)
                enemy.health += resolved_heal
                print("The Great Smashonator heals for {} HP! They have {} health left!".format(resolved_heal,
                                                                                                enemy.health))
                turn = 0
