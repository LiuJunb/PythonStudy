# 1.参数是数组
def get_users(names=[]):
    if names:
        for i in range(len(names)):
            names[i] = i
            print(names[i])
    else:
        print('name=[]')
    return names


users = ['jack', 'li si', 'zha san']

get_users()
# 传递的是引用，内存地址
# get_users(users)

# 传递一个拷贝的副本数组
get_users(users[:])
print(users)












