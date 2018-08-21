from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5&name=jack#comment')

print(type(result))  # <class 'urllib.parse.ParseResult'>
print('===========')
print(result)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
# params='user', query='d=5&name=jack', fragment='comment')

print(result[0], result[1], sep='\n')  # sep='\n'  让每个输出可以换行





