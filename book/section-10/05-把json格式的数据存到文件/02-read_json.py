# 把json格式的数据读取到内存: json.load(file_object)

# 1.导入json类
import json

# 2.将列表数据读取出来
file_name = 'file/json_array.json'
try:
    with open(file_name, 'r') as file_object:
        print(json.load(file_object))
except FileNotFoundError:
    print(' FileNotFoundError ')


# 3.将字典的数据读取出来
user = {
    'name': 'jack',
    'age': 12,
    'sex': 'man'
}
file_name = 'file/user.json'
try:
    with open(file_name, 'r') as file_object:
        print(json.load(file_object))
except FileNotFoundError:
    print(' FileNotFoundError ')







