import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

# 1.偏移两个
result1 = collection.find().sort('name', pymongo.DESCENDING).skip(2)
for res in result1:
    print(res['name'])

print('=======================')
# 2.偏移（分页）
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

print('-----------------------')
# 3.限制个数
results = collection.find().sort('name', pymongo.ASCENDING).limit(2)
print([result['name'] for result in results])



















