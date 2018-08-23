import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'

try:
    # 1.插入一条数据（ 位置填充 ）
    cursor.execute(sql, (id, user, age))
    # 2. 提交事务
    db.commit()
except:
    # 3. 回滚
    db.rollback()

db.close()