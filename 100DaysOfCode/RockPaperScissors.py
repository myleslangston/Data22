import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
computer_choice = random.randint(0, 2)

if player_choice == 0:
    print("You choose Rock!")
elif player_choice == 1:
    print("You choose Paper!")
else:
    print("You choose Scissors!")

if computer_choice == 0:
    print("Computer chose Rock!")
elif computer_choice == 1:
    print("Computer chose Paper!")
else:
    print("Computer chose Scissors!")

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")