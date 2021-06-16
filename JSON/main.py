import json

car_data = {"name": "Tesla", "engine": "electric"}

# car_data_json_string = json.dumps(car_data)  # allows you to store a json file to a variable, as a string
#
# print(car_data_json_string)
# print(type(car_data_json_string))

# with open('new_json_file.json', 'w') as jsonfile:
#     json.dump(car_data, jsonfile)  # "dumps" a variable called car_data into a new json file. Writes to it.

with open("new_json_file.json", 'r') as jsonfile:
    car = json.load(jsonfile)  # allows you to read a json file


print(type(car))
print(car['name'])