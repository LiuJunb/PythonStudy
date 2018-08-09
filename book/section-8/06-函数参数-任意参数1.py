# 1.函数接收任意任意参数( 封装到元组中 )
def get_users1(*names):
    print(names)


get_users1('jack', 'li', 'wang', 'chen')  # ('jack', 'li', 'wang', 'chen')


# 2.函数接收任意任意参数( 封装到元组中 )
def get_users2(name, *names):
    print(name, names)


get_users2('jack', 'li', 'wang', 'chen')  # jack ('li', 'wang', 'chen')


# 3.函数接收任意任意参数( 封装到元组中 )
def get_users3(*names, name):
    print(names, name)


# get_users3('jack', 'li', 'wang', 'chen')  # 这个会报错
get_users3('jack', 'li', 'wang', 'chen', name='dong')  # ('jack', 'li', 'wang', 'chen') dong



