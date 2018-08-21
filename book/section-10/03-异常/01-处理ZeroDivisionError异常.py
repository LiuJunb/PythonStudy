# 1.会发生异常的代码
# print(10/0)  # ZeroDivisionError: division by zero

# 2.02-处理异常：ZeroDivisionError

try:
    print(10/0)
except ZeroDivisionError:
    print('发生了这个异常 ZeroDivisionError')


# 3.02-处理异常：FileNotFoundError
try:
    with open('file/test3.txt') as file_object:
        file_object.readlines()
except FileNotFoundError:
    print('发生了这个异常 FileNotFoundError')

