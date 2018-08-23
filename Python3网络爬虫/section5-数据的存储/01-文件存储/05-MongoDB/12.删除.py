import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

result = collection.remove({'name': 'Jordan'})
print(result)  # {'n': 2, 'ok': 1.0}





