# 默认使用python3的语法

# 1.控制台输出
print ('hello world python3')

# 2.注释：
'''注释的第一种写法'''
# 注释的第二种写法


# 3.定义变量
message = 'liu jun'
first_name = 'liu'
last_name = 'jun'
full_name = first_name + ' ' + last_name
user_name = 'jack  '

# 4.字符串常见的方法
print(message)  # 输出结果 liu jun
print(message.title(), message.upper(), message.lower())  # Liu Jun LIU JUN liu jun

print(first_name + last_name)   # 字符串的拼接
print(full_name)    # liu jun

print(user_name)  # jack
print(user_name.rstrip())   # 仅仅去除尾部的空格
# 还可以剔除字符串开头的空白 lstrip()，或同时剔除字符串两端的空白 strip()

# 5.制表符 和 换行符
print('message')
print('\nmessage')  # 换行符号
print('\tmessage')  # 制表符,缩进tab














