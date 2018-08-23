# 1.函数接收任意任意参数( 封装到元组中 )
def get_users1(*names):
    """遍历元组"""
    for v in names:
        print(v)
    print(names)


get_users1('jack', 'li', 'wang', 'chen')  # ('jack', 'li', 'wang', 'chen')


# 2.函数接收任意任意参数( 封装到元组中 )
def get_users1(name, age, *names):
    print(name, age, names)


get_users1('jun', 12, 'jack', 'li', 'wang', 'chen')  # jun 12 ('jack', 'li', 'wang', 'chen')





