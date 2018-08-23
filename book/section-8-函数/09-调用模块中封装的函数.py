# 1.导入整个模块
# import user
# print(user.get_user_name1('liu', 'jun'))

# import user as u
# print(u.get_user_name1('liu', 'jun'))


# 2.导入模块中特定的函数 - 一个
# from user import get_user_name1
# print(get_user_name1('lao', 'li'))


# 3.导入模块中特定的函数 - 多个
# from user import get_user_name1, get_user_name2
# print(get_user_name1('liu', 'jun'))
# print(get_user_name2('lao', 'li'))

# 4.导入模块中特定的函数 - 多个
# from user import get_user_name1 as getName1, get_user_name2 as getName2
# print(getName1('liu', 'jun'))
# print(getName2('lao', 'li'))


# 5.导入模块中所有的函数
# from user import *
# print(get_user_name1('liu', 'jun'))
# print(get_user_name2('lao', 'li'))

"""导入其它-文件夹-中的模块"""
# 6.导入其它文件夹中的模块
import module.user as user
print(user.get_user_name3('liu', 'jun'))


# 6.导入其它文件夹中的模块
from module.user import *
print(get_user_name2('liu', 'jun'))





