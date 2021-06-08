CarParts = {"wheels", "doors", "exhaust"}
print(CarParts)

ListCarParts = ["wheels", "doors", "exhaust", "exhaust"]
print(set(ListCarParts))

CarParts.add("windows")
print(CarParts)
# a = [1, 2, 2, 3, 3]
#
# print(len(a))
# print(set(a))
# print(len(set(a)))
#
# print('This list has ' + str(len(a)-len(set(a))) + ' duplicates')

x = frozenset([1, 2, 3, 4])
print(x)

