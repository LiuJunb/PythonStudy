import pymysql

# 1.链接数据库
db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')
cursor = db.cursor()

sql = 'UPDATE students SET age = %s WHERE name = %s'

# 2.执行sql语句
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except :
    db.rollback()

db.close()

