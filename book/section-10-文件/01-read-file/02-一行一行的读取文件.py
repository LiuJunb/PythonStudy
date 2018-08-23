# 01.读取文件( 关键字with在不再需要访问文件后将其关闭 )
with open('file/test1.txt') as file_object:
    for line in file_object:
        print(line.rstrip())  # rstrip 去除尾部的换行（空的字符串）



