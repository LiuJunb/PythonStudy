import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students


result1 = collection.find().sort('name', pymongo.DESCENDING)
for res in result1:
    print(res['name'])
























