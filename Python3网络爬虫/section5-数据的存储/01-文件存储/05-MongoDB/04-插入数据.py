import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

student = {
    'id': '20170102',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# 1.如果数据库还不存在那么等到插入数据才会创建数据库
# result = collection.insert(student)

result = collection.insert_one(student)
print(result)  # <pymongo.results.InsertOneResult object at 0x1063995c8>
print(result.inserted_id)  # 5b7ce49a8ffaed09bb5be827


