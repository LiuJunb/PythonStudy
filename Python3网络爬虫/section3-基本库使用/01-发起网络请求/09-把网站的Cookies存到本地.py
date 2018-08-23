from urllib import request
from http import cookiejar

filename = 'LWPCookieJarCookie.txt'
cookie = cookiejar.LWPCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
# build_opener(*handler) 代表可以接收多个handler
opener = request.build_opener(handler)

# 访问的是http协议，不需要证书
response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf8'))

# 将cookie存到本地
cookie.save(ignore_discard=True, ignore_expires=True)

for item in cookie:
    print(item.name + '=' + item.value)
