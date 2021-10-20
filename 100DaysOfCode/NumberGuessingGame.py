import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    guesses = 10
    print(f"You have {guesses} attempts remaining to guess the number.")
elif difficulty == 'hard':
    guesses = 5
    print(f"You have {guesses} attempts remaining to guess the number.")
number = random.randint(1, 101)
game_on = True
while game_on:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The number was {guess}")
        game_on = False
    elif guess > number:
        guesses -= 1
        print(f"Too high.\nGuess again.\nYou have {guesses} attempts remaining to guess the number.")
    elif guess < number:
        guesses -= 1
        print(f"Too Low.\nGuess again.\nYou have {guesses} remaining to guess the number.")




