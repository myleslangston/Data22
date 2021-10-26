import random

easy_level_turns = 10
hard_level_turns = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it, the answer was {answer}!")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 101)
    turns = set_difficulty()
    guess = 0
    while guess != number:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


game()