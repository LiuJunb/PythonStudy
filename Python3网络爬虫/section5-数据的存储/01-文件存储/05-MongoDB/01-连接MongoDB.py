# 启动MongoDB ： sudo mongod
import pymongo

# 1.创建一个 MongoDB 的连接对象
client = pymongo.MongoClient(host='localhost', port=27017)

# or
# client = pymongo.MongoClient('mongodb://localhost:27017/')


