# 导入已经安装好的requests
import requests


def print_line(value):
    print()
    print('============' + value + '============')
    print()


# 1.发起一个get请求
r = requests.get('https://www.baidu.com')
print(type(r))  # <class 'requests.models.Response'>
print(r.status_code)  # 200
print(type(r.text))  # <class 'str'>
print(r.text)
print(r.cookies)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

# 2.发起一个基本的请求

res1 = requests.get('http://httpbin.org/get')
print_line('res1')
print(res1.text)


# 3.发起一个get请求

res2 = requests.get('http://httpbin.org/get?name=jack&age=12')
print_line('res2')
print(res2.text)


# 4.发起一个get请求
params = {
    'name': 'liu jun',
    'age': 20,
    'sex': 'man'
}
res3 = requests.get('http://httpbin.org/get', params=params)
print_line('res3')
print(res3.json())
print(type(res3.json()))  # <class 'dict'>





