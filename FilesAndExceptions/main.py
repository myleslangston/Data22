# file = open("order.txt")  # opens a text file called "order" and saves it to a variable "file". Got to specify file path if not open in pycharm.
                        # File not found error

# x=10
# if x < 10   # Syntax error
#     x += 1

# x = 4/0  # Zero division error

# x = 4 + "hello"   # Type error

# try:
#     # file = open("order.txt")
# except:
#     print(
#         "There has been an error! Panic!")  # as soon as an error is found in the try loop, immediately goes to the except loop, forgets anything below the error.

try:
    # file = open("order.txt")
    x = 4/0
except FileNotFoundError:
    print("There has been an error!")  # cam separate out except clauses for specific errors.
except ZeroDivisionError:
    print("You can't divide by 0 you fool!")
    raise  # 'catches' the error. one of the except blocks have to catch the error.
