# 01.读取文件( 关键字with在不再需要访问文件后将其关闭 )
with open('file/test1.txt') as file_object:
    contents = file_object.read()  # 在读到文本的尾部时返回一个空的字符窜
    print(contents)



