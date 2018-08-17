# 1.统计文章单词数函数
def counts_words(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print('file not found error')
        pass  # 什么事情都不做
    else:
        words = contents.split()
        num_words = len(words)
        return num_words


# 2.调用函数
file_names = ['file/Test.txt', 'file/test3.txt']

for file_name in file_names:
    print(counts_words(file_name))


