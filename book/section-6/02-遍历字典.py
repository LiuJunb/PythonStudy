# 1.定义一个字典
person = {
    "name": "jack",
    "age": 12,
    "sex": 'man',
    'first_name': 'jack'
}


# 2.遍历字典
for key, value in person.items():
    print(key, value)
    # name jack
    # age 12
    # sex man


print('---遍历字典中所有的key---')
# 3.遍历字典中所有的key
for key in person.keys():
    print(key, person[key])
    # name jack
    # age 12
    # sex man
print(person.keys())  # dict_keys(['name', 'age', 'sex'])
print(type(person.keys()))  # <class 'dict_keys'>

print(sorted(person.keys()))  # ['age', 'name', 'sex']
# print(person.keys()['age'])  # TypeError: 'dict_keys' object is not subscriptable
# print(person.keys().reverse())  # AttributeError: 'dict_keys' object has no attribute 'reverse'


print('---遍历字典中所有的value---')
# 4.遍历字典中所有的value
for value in person.values():
    print(value)


print('---遍历字典中所有的value,并去除重复---')
# 5.遍历字典中所有的value,并去除重复
for value in set(person.values()):
    print(value)







