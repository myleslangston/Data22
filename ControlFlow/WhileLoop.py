# x = 0
#
# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1

UserBool = True


while UserBool:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) < 120:
        UserBool = False
        print(f"Your age is {age}")
    else:
        print("Please provide your answer as a number")


