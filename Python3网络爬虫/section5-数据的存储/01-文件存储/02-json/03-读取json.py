import json

with open('./text.json', 'r') as fp:
    str = fp.read()
    print(type(str))
    # 1.将字符串转成json （ load  与 loads ）
    data = json.loads(str)
    print(data)
    print(type(data))  # <class 'list'>

    print(data[0]['name'])
    print(data[0].get('name'))

    print(data[0].get('age'))
    print(data[0].get('age', 25))


print('==========================')

with open('./text.json', 'r') as fp:
    data = json.load(fp)
    print(data)