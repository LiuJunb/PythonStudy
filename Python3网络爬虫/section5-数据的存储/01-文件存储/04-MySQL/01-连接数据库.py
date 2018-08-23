import pymysql

# 1.链接数据库
db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306)
# 2.拿到执行数据库的游标
cursor = db.cursor()
# 3.执行一个sql
cursor.execute('SELECT VERSION()')
# 4.拿到第一条数据
data = cursor.fetchone()
print('Database version:', data)  # Database version: ('8.0.12',)
# 5.创建一个数据库：数据库名称叫做 spiders。默认编码为 utf-8
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# 6.关闭数据的链接
db.close()