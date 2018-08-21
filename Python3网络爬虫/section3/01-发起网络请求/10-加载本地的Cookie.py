from urllib import request
from http import cookiejar

# 带着cookie去访问这个页面
file_name = 'LWPCookieJarCookie.txt'
cookie = cookiejar.LWPCookieJar()
cookie.load(file_name, ignore_discard=True, ignore_expires=True)

handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(handler)

response = opener.open('http://www.baidu.com')

print(response.read().decode('utf8'))

