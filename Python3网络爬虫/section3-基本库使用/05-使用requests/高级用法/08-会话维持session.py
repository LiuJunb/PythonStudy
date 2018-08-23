import requests


def print_line(value):
    print()
    print('============' +value+ '=============')
    print()


print_line('1.获取cookie(不同一个会话)')
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)


print_line('2.使用session来维持会话cookie(同一个会话)')
# Session 在平常用到的非常广泛，可以用于模拟在一个浏览器中打开同一站点的不同页面
s2 = requests.Session()
s2.get('http://httpbin.org/cookies/set/number/123456789')
r2 = s2.get('http://httpbin.org/cookies')
print(r2.text)






