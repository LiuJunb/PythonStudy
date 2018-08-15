# 01.读取文件( 关键字with在不再需要访问文件后将其关闭 )
with open('file/test1.txt') as file_object:
    lines = file_object.readlines()  # 拿到文件中的行的集合

# 遍历行的集合
for line in lines:
    print(line.rstrip())

print('==========================')

str = ''
for line in lines:
    str += line.strip().rstrip()   # 去除字符前面和后面的空格

print(str)

# 判断一个字符是否在一个字符串中
print('python' in str)





