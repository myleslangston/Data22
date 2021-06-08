# generate random numbers between 1 and 9
# get the user to input
    # hide inputted number
    #and guess the number
        # respond too high or too low
    # if right game ends


import random
wrong_guess = 0

number = random.randint(1, 9)

guess = int(input("Please choose a number between 1 and 9..."))

while guess != number:

    if guess > number:
        print("Number too high")
        wrong_guess += 1

        guess = input("Try again...")

    elif guess < number:
        print("Number too high")
        wrong_guess += 1

        guess = input("Try again...")

    else:
        print("Congratulations, you have won the game")


