import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://3.68.198.197:27017")

db = client['starwars']

luke = db.characters.find_one({"name": "Luke Skywalker"}, {"name": 1})
pprint(luke)

