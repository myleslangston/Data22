# student_1 = {"name": "Susan",
#              "stream": "tech",
#              "completed_lessons": 4,
#              "completed_lesson_names": ["variables", "data_types", "set_up"]}
#
# student_1["completed_lessons"] = 3
#
# print(student_1["completed_lessons"])
#
# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])
#
# print(student_1.keys())
# print(student_1.values())

my_passport = {"FirstName": "Myles",
               "LastName": "Langston",
               "Nationality": "British",
               "DOB": "31/03/1997",
               "PlaceOfBirth": "Aberystwyth",
               "DateOfIssue": "07/05/2017"}

print(my_passport.keys())
print(my_passport.values())

my_passport["PlacesVisited"] = ["SriLanka", "Canada", "CostaRica", "SouthAfrica"]

print(my_passport)

