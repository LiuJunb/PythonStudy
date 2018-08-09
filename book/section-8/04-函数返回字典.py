# 1.函数返回值是字典
def get_user_info(fist_name, last_name):
    person = {
        'first': fist_name,
        'last': last_name,
        'full_name': fist_name + ' ' + last_name,
    }
    return person


print(get_user_info('liu', 'jun'))



