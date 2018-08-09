# 1.定义一个字典( 其实就是 HashMap)

person = {'name': 'jack', 'age': 12}

# 打印字典
print(person)  # {'name': 'jack', 'age': 12}

# 获取字典中的key对应的值
print(person['name'])  # jack
# print(person.age)  # AttributeError: 'dict' object has no attribute 'age'

# 添加字典中的key-value
person['x'] = 100.00
person['y'] = 123.23
print(person)  # {'name': 'jack', 'age': 12, 'x': 100.0, 'y': 123.23}

# 创建空的字典
animal = {}
animal['name'] = 'animal'
animal['age'] = 1
animal['sex'] = True
print(animal)  # {'name': 'animal', 'age': 1, 'sex': True}

# 删除字典中对应的key-value
del animal['sex']
print(animal)  # {'name': 'animal', 'age': 1}










