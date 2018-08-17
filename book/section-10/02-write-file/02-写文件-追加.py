# 1.把字符串写入到文件中( 如果文件没有会新建文件,但是文件夹必须有 )
file_name = 'file/test2.txt'

# 2.打开文件（ 只写模式 ）
with open(file_name, 'a') as file_object:
    # 3.不会覆盖之前的内容
    file_object.write('I love you python \n')
    file_object.write('I love you java c \n')

