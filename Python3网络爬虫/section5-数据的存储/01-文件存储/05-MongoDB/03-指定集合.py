import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

# 1.声明了一个 Collection 对象
collection = db.students
# or
# collection = db['students']



