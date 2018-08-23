import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w') as file:
    # 1.将字典数列转成字符串
    print(type(json.dumps(data)))  # <class 'str'>
    file.write(json.dumps(data, indent=2,  ensure_ascii=False))  # indent=2 相当于格式化json
    # 如果字典中带有中文的内容我们需要设置 ensure_ascii 参数为 False 才可正常写入中文

with open('data2.json', 'w') as fp:
    # 2.直接保存对象
    json.dump(data, fp)