from HigherLowerData import data
import random


def get_random_names():
    """Get's random account from data"""
    return random.choice(data)


def check(comparison, a_count, b_count):
    if a_count > b_count:
        return comparison == 'a'
    else:
        return comparison == 'b'


score = 0
game_continue = True
choice_a = get_random_names()
choice_b = get_random_names()
while game_continue:
    choice_a = choice_b
    choice_b = get_random_names()
    while choice_a == choice_b:
        choice_b = get_random_names()

    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print("VS")
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    correct = check(guess, choice_a['follower_count'], choice_b['follower_count'])
    if correct:
        score += 1
        print("You're right.")
    else:
        game_continue = False
        print(f"Sorry, you lost! Final score: {score}")
