# 1.if 语句的使用
cars = ['bm', 'ca', 'bc', 'jl']

for value in cars:
    if value == 'bm':
        print('宝马')
    elif value == 'ca':
        print('长安')
    else:
        print('其它')

if True:
    print('True')


# 2.比较字符窜是否相等
print('bm' == cars[0])  # True
print('ca' == cars[1])  # True
print('CA' == cars[1])  # False  区分大小写
print('CA' == cars[1].upper())  # True

# 3.多个条件
if cars[0] == 'bm' and cars[1] == 'ca':
    print('True')

if cars[0] == 'bm' or cars[1] == 'CA':
    print('True')








