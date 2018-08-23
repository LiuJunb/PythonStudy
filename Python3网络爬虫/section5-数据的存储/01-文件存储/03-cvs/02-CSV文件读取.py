import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    # 1.先拿到csv.reader
    reader = csv.reader(csvfile)
    print(type(reader))  # <class '_csv.reader'>
    # 2.遍历每一行
    for row in reader:
        print(row)

print('===================')
with open('datadict.csv', 'r', encoding='utf-8') as csvfile:
    # 1.先拿到csv.reader
    reader = csv.reader(csvfile)
    print(type(reader))  # <class '_csv.reader'>
    # 2.遍历每一行
    for row in reader:
        print(row)