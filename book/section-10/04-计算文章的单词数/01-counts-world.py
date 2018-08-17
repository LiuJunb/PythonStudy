# 1.统计文章单词数函数
def counts_words(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('file not found error')
    else:
        words = contents.split()
        num_words = len(words)
        print(contents)
        print('----------')
        print(words)
        print('----------')
        print(num_words)


# 2.调用函数
file_name = 'file/test2.txt'
counts_words(file_name)

