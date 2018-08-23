import pymysql

# 1.链接数据库
db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')
cursor = db.cursor()

sql = 'CREATE TABLE IF NOT EXISTS students ' \
      '(id VARCHAR(255) NOT NULL, ' \
      'name VARCHAR(255) NOT NULL, ' \
      'age INT NOT NULL, ' \
      'PRIMARY KEY (id))'

# 2.执行sql语句
cursor.execute(sql)
db.close()