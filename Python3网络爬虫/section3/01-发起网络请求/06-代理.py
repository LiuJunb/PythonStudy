from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener, HTTPSHandler
import ssl

# 这个代理要起作用必须要手动：实现对下面ip和端口的监听
proxy_handler = ProxyHandler({
     'http': 'http://127.0.0.1:51599',
     'https': 'https://127.0.0.1:51599'
})
c = ssl._create_unverified_context()
s = HTTPSHandler(context=c)
opener = build_opener(s, proxy_handler)

resposne = opener.open('http://httpbin.org/get')
print(resposne.read().decode('utf-8'))






