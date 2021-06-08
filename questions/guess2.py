import random
correct_number = random.randint(1,100)
guess_counter = 1
guesses = []
guess = int(input("Welcome to hell, to escape you must guess what number I am thinking between 1 and 100:  "))

while guess != correct_number:

    if guess < correct_number:
        guess = int(input("Too low! Guess again..."))
        guesses.append(guess)
        guess_counter += 1
    elif guess > correct_number:
        guess = int(input("Too high! Guess again..."))
        guesses.append(guess)
        guess_counter += 1

if guess == correct_number:
    print("Congratulations, here is a certificate, please show this to Hades and he will let you go")
    print(f"You guessed {guess_counter} times")


