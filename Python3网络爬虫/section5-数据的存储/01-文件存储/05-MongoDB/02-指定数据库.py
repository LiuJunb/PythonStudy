import pymongo

# 1.创建一个 MongoDB 的连接对象
client = pymongo.MongoClient(host='localhost', port=27017)

# 2.链接数据库
db = client.test

# or
# db = client['test']








