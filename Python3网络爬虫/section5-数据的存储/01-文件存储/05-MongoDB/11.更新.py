import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

filter = {'name': 'Liujun'}

student = collection.find_one(filter)
# print(student)  # {'_id': ObjectId('5b7ce49a8ffaed09bb5be827'), 'id': '20170105', 'name': 'Liujun', 'age': 20, 'gender': 'male'}

# 1.更新数据
student['age'] = 30
# 2.执行更新
result = collection.update(filter, student)
print(result)  # {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}


# 3.推荐更新的方式 $set ：
# 这样可以只更新 student 字典内存在的字段，如果其原先还有其他字段则不会更新，也不会删除。
# 而如果不用 $set 的话则会把之前的数据全部用 student 字典替换，如果原本存在其他的字段则会被删除
student['age'] = 29
result2 = collection.update(filter, {'$set': student})
result2 = collection.update(filter, {'$set': {'gender': 'man'}})





