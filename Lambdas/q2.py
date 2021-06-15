def given_number(n):
    return lambda num1: num1 * n

result = given_number(2)
print(result(15))
result = given_number(3)
print(result(15))
result = given_number(4)
print(result(15))
result = given_number(5)
print(result(15))