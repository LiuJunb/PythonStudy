from urllib import request, parse
import ssl

context = ssl._create_unverified_context()



url = 'http://httpbin.org/post'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',   # 伪装火狐浏览器
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey',
    'love': 'Playing'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header('Host', 'httpbin.org')

resposne = request.urlopen(req, context=context)

print(resposne.read().decode('utf-8'))







