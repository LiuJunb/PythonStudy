# 1.导入系统urllib类中的request类
import urllib.request
import ssl

# 2.设计urllib 不进行证书验证
context = ssl._create_unverified_context()

# 3.百度的https就是一个重新加载HTTP而已，<noscript></noscript>就是对不支持javascript的浏览器的一个支持，采用refresh的方法，还是重定向到http了
response = urllib.request.urlopen('https://www.baidu.com', context=context)

# response = urllib.request.urlopen('https://www.python.org', context=context)
print(type(response))  # <class 'http.client.HTTPResponse'>
# print(response.read().decode('utf-8'))


# 4.HTTPResposne 类型的对象，
# 它主要包含的方法有 read()、readinto()、getheader(name)、getheaders()、fileno() 等方法
# 和 msg、version、status、reason、debuglevel、closed 等属性
print(response.getheaders())
print(response.getheader('Accept-Ranges'))
print(response.getheader('Server'))
print(response.status, response.version)









