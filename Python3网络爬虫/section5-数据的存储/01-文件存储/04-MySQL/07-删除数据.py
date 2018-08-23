import pymysql

db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'

sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# print(sql)  # DELETE FROM  students WHERE age > 20

try:
    if cursor.execute(sql):
        print('Successful')
        db.commit()
except :
    print('Failed')
    db.rollback()


db.close()