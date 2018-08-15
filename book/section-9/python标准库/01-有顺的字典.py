# 1.从 collections 模块中导入 OrderedDict类
from collections import OrderedDict

# 2.实例化有顺序的字典
order_dict = OrderedDict()

# 3.给字典添加数字
order_dict['name'] = 'jack'
order_dict['age'] = 20
order_dict['sex'] = 'man'
order_dict['love'] = ['play game', 'swing', 'running']

# 4.遍历字典

for key, value in order_dict.items():
    print(type(value))
    if isinstance(value, int):
        print('=====================')
        value = str(value)
    elif isinstance(value, list):
        print('=====================')
        value = list(value)

    print(key + '=' + value)

