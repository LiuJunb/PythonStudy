# 1.元组简介：
# 元组类似数列。跟数列不一样的是，元组里的元素不能被修改

# 2.定义元组

tuple_arr = (1, 2, 3, 4, 5)

# 3.获取元组里面的值
print(tuple_arr[0])

# 修改元组中的值
# tuple_arr[0] = 100  TypeError: 'tuple' object does not support item assignment

# 4.遍历元组

for value in tuple_arr:
    print(value)

# 5.给元组变量重新赋值
tuple_arr = (300, 100, 200)  # 这个会覆盖以前的元组
print(tuple_arr)









