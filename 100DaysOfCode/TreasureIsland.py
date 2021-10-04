print("Welcome to Treasure Island.\n"
      "Your mission is to find the treasure.")
cross_road = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n")
if cross_road == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if lake == "wait":
        house = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow ans one blue. Which colour do you choose?\n")
        if house == "yellow":
            print("Congratulations. You win!")
        else:
            print("Unlucky, game over!")
    else:
        print("Unlucky, game over!")
else:
    print("Unlucky, game over!")