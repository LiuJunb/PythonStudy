# 1.创建字典的列表
persons = [
    {'name': 'jack1', 'age': 1},
    {'name': 'jack2', 'age': 2},
    {'name': 'jack3', 'age': 3},
]

print(persons)  # [{'name': 'jack1', 'age': 1}, {'name': 'jack2', 'age': 2}, {'name': 'jack3', 'age': 3}]


# 2.随机生产多个字典的列表
animals = []
for value in range(0, 10):
    cat = {'name': 'cat'+str(value), 'age': value}
    animals.append(cat)
print(animals)


# 3.显示前5个cat
for cat in animals[0:5]:
    print(cat)

# 4.在字典中存错列表
pizza ={
    'name': 'pizza1',
    'price': 100,
    'size': [1, 2, 3, 4, 5]
}

print(pizza['name'])
print(pizza['price'])
print(pizza['size'])

print('---')
for key, value in pizza.items():
    print(key, value, type(value))
    if isinstance(value, list):  # 盘value 是否是一个 数列
        for v in value:
            print(v)










