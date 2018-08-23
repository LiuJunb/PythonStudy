import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

# 1.查询age = 20
result1 = collection.find({'age': 20})
# print(result1)
for res in result1:
    print(res)

print('===========2.查询age < 20============')
# 2.查询age < 20
result2 = collection.find({'age': {'$lt': 20}})
for res in result2:
    print(res)

print('===========3.查询 age = 10 或者 age = 11 或者 age = 20 ============')
result3 = collection.find({'age': {'$in': [10, 11, 20]}})
for res in result3:
    print(res)

print('===========4.查询 20 > age > 10 =====可以,并且and=======')
result4 = collection.find({'age': {'$lt': 20, '$gt': 10}, 'id': {'$regex': '^20170104$'}})
for res in result4:
    print(res)


print('===========5.查询 20 > age > 10 ======可以======')
result4 = collection.find({'$where': 'obj.age < 20 & obj.age > 10'})
for res in result4:
    print(res)


