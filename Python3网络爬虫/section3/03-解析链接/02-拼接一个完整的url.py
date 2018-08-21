from urllib.parse import  urlunparse


data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6&id=100', 'comment']

print(urlunparse(data))



