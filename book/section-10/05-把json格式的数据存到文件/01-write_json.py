# 把json 格式的数据存到本地 :json.dump(json_array, file_object)

# 1.导入json类
import json

# 2.将列表数据存到本地
json_array = [1, 2, 3, 4]
file_name = 'file/json_array.json'
try:
    with open(file_name, 'w') as file_object:
        # file_object.write('string')
        json.dump(json_array, file_object)  # 将json数据存到本地
except FileNotFoundError:
    print(' FileNotFoundError ')


# 3.将字典存到本地
user = {
    'name': 'jack',
    'age': 12,
    'sex': 'man'
}
file_name = 'file/user.json'
try:
    with open(file_name, 'w') as file_object:
        json.dump(user, file_object)  # 将json数据存到本地
except FileNotFoundError:
    print(' FileNotFoundError ')







