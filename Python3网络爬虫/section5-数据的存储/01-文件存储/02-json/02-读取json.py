import json


# 注意里面的json字符串的key和value必须是双引号
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
# 1.将字符串转成json （ load  与 loads ）
data = json.loads(str)
print(data)
print(type(data)) # <class 'list'>

print(data[0]['name'])
print(data[0].get('name'))

print(data[0].get('age'))
print(data[0].get('age', 25))
