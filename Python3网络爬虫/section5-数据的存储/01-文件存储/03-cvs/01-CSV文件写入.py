import csv

with open('data.csv', 'w') as csvfile:

    # 1.拿到csv.writer
    writer = csv.writer(csvfile, delimiter=' ')  # delimiter是修改列与列之间的分隔符（ 默认是逗号 ）
    # 2.开始一行一行插入数据：writerow
    writer.writerow(['id', 'name', 'age'])  # 插入表格的头部
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
    writer.writerows([['10004', 'Mike', 20], ['10005', 'Bob', 22], ['10006', 'Jordan', 21]])

    # 3.写入字典格式的数据


# 如果我们要写入中文内容的话可能会遇到字符编码的问题
with open('datadict.csv', 'w', encoding='utf-8') as csvfile:
    # 1.定义表格的头部
    fieldnames = ['id', 'name', 'age']
    # 2.拿到cvs.writer
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 3.先写入表格头部
    writer.writeheader()
    # 4.给表格插入每一行
    writer.writerow({'id': '10001', 'name': '刘军', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
