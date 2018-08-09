# 1.返回值类型
def get_full_name(first_name, last_name):
    """获取全名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


print(get_full_name('liu', 'jun'))


# 2.返回值类型
def get_full_name(first_name, last_name, exp=''):
    """获取全名"""
    full_name = first_name + ' ' + last_name
    if exp:
        """如果exp不为空的字符串"""
        print('exp=' + exp)
    else:
        """如果exp为空的字符串"""
        print('exp=''')
    return full_name.title()


print(get_full_name('liu', 'jun'))
print('------------')
print(get_full_name('liu', 'jun', 'ha'))










