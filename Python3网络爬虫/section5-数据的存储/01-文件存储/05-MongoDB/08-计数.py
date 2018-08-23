import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['test']
collection = db['students']

count1 = collection.find({'age': 20}).count()
print(count1)

print('===================')
# count2 = db.students.find().count()
# print(count2)

count3 = collection.count_documents({})
print(count3)





