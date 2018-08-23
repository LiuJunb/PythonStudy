# 1.导入系统urllib类中的request类
import urllib.request
import ssl
import urllib.parse
import urllib.error
import socket

# 2.设计urllib 不进行证书验证
context = ssl._create_unverified_context()
# 3.准备提交的表单 data 。传递了一个参数 word，值是 hello。它需要被转码成bytes（字节流）类型
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')

try:

    response = urllib.request.urlopen('http://httpbin.org/post', context=context, data=data, timeout=0.1)

except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time out')

else:
    print(response.read().decode('utf-8'))  # urllib.error.URLError: <urlopen error timed out>










