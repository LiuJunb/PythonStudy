import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

print('========1.查询一条===========')
# result = collection.find_one({'name': 'Jordan'})
# print(result)  # {'_id': ObjectId('5b7ce49a8ffaed09bb5be827'), 'id': '20170105', 'name': 'Jordan', 'age': 20, 'gender': 'male'}

print('========1.查询一条,通过 _id ===========')

result1 = collection.find_one({'_id':ObjectId('5b7ce49a8ffaed09bb5be827')})
print(result1)

print('========2.查询多条===========')
result2 = collection.find({'age': 20})
print(result2)  # <pymongo.cursor.Cursor object at 0x109f66c88>
for res in result2:
    print(res)

# client.shutdownServer()
