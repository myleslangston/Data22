import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

# droids = db.characters.find({"species.name": "Droid"})
#
# print([droid["name"] for droid in droids])

# for droid in droids:
#     print(droid["name"])

# Find the height of Darth Vader, only return results for the name and the height.
# Find all characters with yellow eyes, only return results for the names of the characters.
# Find male characters. Limit your results to only show the first 3.
# Find the names of all the humans whose homeworld is Alderaan.
# What is the average height of female characters?
# Which character(s) is/are the tallest?

# darth_vader = db.characters.find_one({"name": "Darth Vader"})
#
# print([darth_vader["name"], darth_vader["height"]])

# yellow_eyes = db.characters.find({"eye_color": "yellow"})
#
# print([yellow["name"] for yellow in yellow_eyes])

# male_characters = db.characters.find({"gender": "male"})
#
# list = [male["name"] for male in male_characters]
#
# print(list[:3])

# human_alderaan = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"})
#
# print([hum_ald["name"] for hum_ald in human_alderaan])

# female_char = db.characters.find({"gender": "female", "height": {"$exists": True}})
#
# female_heights = [females["height"] for females in female_char]
# avg_height = sum(female_heights)/len(female_heights)
# print(avg_height)

# characters = db.characters.find({"height": {"$exists": True}})
# heights = [character["height"] for character in characters]
# print(max(heights))
# max_height = db.characters.find({"height": max(heights)})
# print([person["name"] for person in max_height])
#
max_height = next(db.characters.aggregate(
    [
        {"$group": {
            "_id": None, "max_height": {"$max": "$height"}
        }}
    ]
))["max_height"]

for tallest in db.characters.find({"height": max_height}):
    print(tallest["name"], tallest['height'])