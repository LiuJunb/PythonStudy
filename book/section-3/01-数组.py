# 1.数组
arr = [1, 2, 3, 4]
print(arr)  # [1, 2, 3, 4]

# 获取
print(arr[0])   # 1
# 修改
arr[0] = 100
print(arr)  # [100, 2, 3, 4]
# 添加
arr.append(200)
print(arr)  # [100, 2, 3, 4, 200]
# 插入
arr.insert(1, 300)
print(arr)  # [100, 300, 2, 3, 4, 200]
# 删除 指定位置的元素
del arr[0]
print(arr)  # [300, 2, 3, 4, 200]
del arr[0:2]    # 删除角标是2以前的值
print(arr)  # [3, 4, 200]
# 删除 尾部元素
print(arr.pop())    # 返回删除的元素
print(arr)  # [3, 4]
# 删除 指定的值 remove()
arr.insert(0, 4)
print(arr)
arr.remove(4)   # 只删除第一个指定的值
print(arr)  # [3]

# 数组的排序 sort()
cars = ['bm', 'bt', 'jl', 'ca'];
print(cars)  # ['bm', 'bt', 'jl', 'ca']

cars.sort()
print(cars)  # ['bm', 'bt', 'ca', 'jl']
cars.sort(reverse=True)
print(cars)  # ['jl', 'ca', 'bt', 'bm']

# 数据的排序-不影响源数组 sorted()
print('--------------')
print(sorted(cars))
print(cars)

# 数组的取反 reverse()
cars.reverse()
print(cars)

# 数组的长度 len()
print(len(cars))
























