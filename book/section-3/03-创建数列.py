# 1.创建数组
arr = range(10)  # 0 - 10
print(arr)  # range(0, 10)
print(list(arr))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in arr:
    print(value)

print('----')

for key in range(0, 3):
    print(key)

arr1 = range(0, 10, 2)
print(list(arr1))  # [0, 2, 4, 6, 8]

arr1 = range(10, 2)
print(list(arr1))  # []


# 2.定义一个数组（数列）

arr2 = [value*2 for value in arr]
print(list(arr))
print(arr2)

# 等同于
arr3 = []
for value in arr:
    arr3.append(value*2)
print(arr3)

# 3.切片
players = ['j', 'i', 'p', 'k']
print(players[0:3])  # ['j', 'i', 'p']


# 4.遍历切片
for value in players[-3:]:
    print(value)

# 5.复制列表
copy_players = players[:]
print(copy_players)  # ['j', 'i', 'p', 'k']





