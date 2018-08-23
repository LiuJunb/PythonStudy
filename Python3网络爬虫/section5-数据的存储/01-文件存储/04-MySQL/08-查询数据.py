import pymysql

db = pymysql.connect(host='localhost', user='root', password='rootadmin', port=3306, db='spiders')

cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'

try:
    if cursor.execute(sql):
        print('counts:', cursor.rowcount)
        # one_line = cursor.fetchone()
        # print(one_line)

        # fetchall() 会将结果以元组形式全部返回，如果数据量很大，那么占用的开销会非常高
        all_row = cursor.fetchall()
        print(all_row)  # (('20120001', 'Bob', 20), ('20120002', 'Bob', 20))
        print(type(all_row))  # <class 'tuple'>
        for row in all_row:
            print(row)

except:
    print('error')

db.close()