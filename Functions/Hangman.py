

import random
words = ["rainbow", "ticket", "computer", "programming", "database", "players", "python", "mindblown"]
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 20

while turns > 0:
    failed = 0
    for letter in word:
        if letter in guesses:
            print(letter)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win. The word was ", word)
        break

    guess = input("Guess a letter ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Incorrect")

        print(f"You have {turns} more guesses left")

        if turns == 0:
            print("You have lost. Better luck next time")

