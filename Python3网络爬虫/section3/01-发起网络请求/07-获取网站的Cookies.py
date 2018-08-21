from urllib import request
from http import cookiejar


cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
# build_opener(*handler) 代表可以接收多个handler
opener = request.build_opener(handler)

# 访问的是http协议，不需要证书
response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf8'))

for item in cookie:
    print(item.name + '=' + item.value)
