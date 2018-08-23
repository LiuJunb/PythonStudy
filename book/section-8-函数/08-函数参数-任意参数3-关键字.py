# 1.函数接收任意任意关键字参数( 封装到元组中 )
def get_users1(name, age, **loves):
    user = {}
    user['name'] = name
    user['age'] = age
    if loves:
        print(loves)  # 获取到的是一个字典
        for key, value in loves.items():
            user[key] = value
    else:
        print(loves)
    return user


print(get_users1('liu jun', 12))
print('-------------------')
print(get_users1('liu jun', 12, china=2, math=3))


# name, 位置参数
# age,  位置参数

# *firends, 可变普通参数
# **loves)  可变关键字参数
def get_users2(name, age, *firends, **loves):
    user = {}
    user['name'] = name
    user['age'] = age
    if loves:
        print(loves)  # 获取到的是一个字典
        for key, value in loves.items():
            user[key] = value
    else:
        print(loves)

    if firends:
        print(firends)
        for i in range(len(firends)):
            key = 'f' + str(i)
            user[key] = firends[i]
    else:
        print(firends)

    return user


print('\n\n')
print(get_users2('liu jun', 12, 'firends 1', 'firends 2'))
print('-------------------')
print(get_users2('liu jun', 12, 'firends 1', china=2, math=3))





