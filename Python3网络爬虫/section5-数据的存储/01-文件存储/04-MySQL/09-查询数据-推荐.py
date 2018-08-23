import pymysql

db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')

cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'

try:
    if cursor.execute(sql):
        print('counts:', cursor.rowcount)
        # cursor 偏移指针
        one_line = cursor.fetchone()
        while one_line:
            print(one_line)
            one_line = cursor.fetchone()

except:
    print('error')

db.close()