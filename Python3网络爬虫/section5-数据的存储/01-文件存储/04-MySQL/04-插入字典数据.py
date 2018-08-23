import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())  # id, name, age
# print(keys)
values = ', '.join(['%s'] * len(data))  # %s, %s, %s
# print(values)

# print('table={table}')  # table={table}
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# print(sql)  # INSERT INTO students(id, name, age) VALUES (%s, %s, %s)

# print(data.values())  # dict_values(['20120001', 'Bob', 20])
# print(tuple(data.values()))  # ('20120001', 'Bob', 20)   将字典转成values

try:
   if cursor.execute(sql, tuple(data.values())):
       print('Successful')
       db.commit()
except:
    print('Failed')
    db.rollback()
db.close()