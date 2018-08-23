import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

students = [
    {
        'id': '20170110',
        'name': 'Jordan',
        'age': 10,
        'gender': 'male'
    },
    {
        'id': '20170111',
        'name': 'Jordan',
        'age': 11,
        'gender': 'male'
    }
]

# 1.如果数据库还不存在那么等到插入数据才会创建数据库
results = collection.insert_many(students)
# result = collection.insert([student1, student2])
print(results)  # <pymongo.results.InsertManyResult object at 0x108150488>
