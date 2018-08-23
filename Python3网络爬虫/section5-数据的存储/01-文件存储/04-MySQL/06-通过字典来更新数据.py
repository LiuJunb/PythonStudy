import pymysql

# 1.链接数据库
db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

table = 'students'
# print(data.keys()) # dict_keys(['id', 'name', 'age'])
keys = ', '.join(data.keys())
# print(keys)    # id, name, age
values = ', '.join(['%s'] * len(data))
# print(values)  # %s, %s, %s

# ON DUPLICATE KEY UPDATE :这个的意思是如果主键已经存在了，那就执行更新操作
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
# print(sql)  INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
# print(sql)
#  INSERT INTO students(id, name, age) VALUES (%s, %s, %s)
#  ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s

# if cursor.execute(sql, tuple(data.values()) * 2):
#     print('Successful')
#     db.commit()

# print(tuple(data.values())*2)  # ('20120001', 'Bob', 21, '20120001', 'Bob', 21)

# 2.执行sql语句
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except :
    print('Failed')
    db.rollback()

db.close()

