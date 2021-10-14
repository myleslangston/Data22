def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
    n1 = float(input("Please choose a number:\n"))
    for action in operations:
        print(action)
    carry_on = True
    while carry_on:
        n2 = float(input("Please choose another number:\n"))
        symbol = input("Pick an operation: ")
        value = operations[symbol](n1, n2)
        print(f"{n1} {symbol} {n2} = {value}")
        another_calc = input(f"Type 'y' if you would like to carry on calculating with {value}, or type 'n' to start again: ")
        if another_calc == 'y':
            n1 = value
        else:
            carry_on = False
            calculator()


calculator()
