from urllib import request, error
import ssl

context = ssl._create_unverified_context()
try:
    # urlopen( 参数一可以使用request对象也可以是str字符串 , )
    resposne = request.urlopen('http://cuiqingcai.com/index.htm', context=context)

except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print('===========')
    print(e.headers)

except error.URLError as e:
    print('URLError是HTTPError的父类')
    print(e.reason)

else:
    print('网络请求成功：' + resposne.read().decode('utf-8'))

