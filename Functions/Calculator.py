# programme to build a calculator

# function defines addition
def add(int1: int, int2: int):
    return int1 + int2


# function defines subtraction
def subtract(int1: int, int2: int):
    return int1 - int2


# function defines multiplication
def multiply(int1: int, int2: int):
    return int1 * int2


# function defines division
def division(int1: int, int2: int):
    return int1 / int2


print("Welcome to the Calculator. Please select an operation...")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        int1 = float(input("Enter first number: "))
        int2 = float(input("Enter second number: "))

        if choice == '1':
            print(int1, "+", int2, "=", add(int1, int2))

        elif choice == '2':
            print(int1, "-", int2, "=", subtract(int1, int2))

        elif choice == '3':
            print(int1, "*", int2, "=", multiply(int1, int2))

        elif choice == '4':
            print(int1, "/", int2, "=", division(int1, int2))
        break
    else:
        print("Invalid Input")