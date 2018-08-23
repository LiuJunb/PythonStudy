# 1.定义一个数列
car = [
    'bm',
    'ca',
    'jl'
]

copyCat1 = []
copyCat2 = []

# 2.切片拷贝数列
copyCat1 = car[:]
print(copyCat1)

# 3.while 拷贝数列
while car:
    copyCat2.append(car.pop())

print(car)

print(copyCat2)
print(type(copyCat2))

copyCat2.reverse()  # 返回结果为 None
print(copyCat2)





























