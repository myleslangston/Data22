numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda num: num % 2 == 0, numbers))
odd = list(filter(lambda num: num % 2 != 0, numbers))
print(even)
print(odd)
