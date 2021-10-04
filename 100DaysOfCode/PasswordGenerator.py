import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my Password Generator")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many numbers would you like?\n"))

random_letters = random.sample(letters, num_letters)
random_numbers = random.sample(numbers, num_numbers)
random_symbols = random.sample(symbols, num_symbols)

password = ""

for char in range(1, num_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, num_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

for char in range(1, num_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym

rand_pass = ''.join(random.sample(password, len(password)))
print(rand_pass)