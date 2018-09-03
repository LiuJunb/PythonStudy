# http://www.xicidaili.com/
# 西刺免费代理
from urllib.error import  URLError
from urllib.request import ProxyHandler, build_opener

proxy = '120.24.152.123:3128'  # 可用https
# proxy = '111.155.116.234:8123'  # 可用 http


# proxy = '111.155.116.221:8123'  # 不可用
# proxy = '111.155.116.236:8123'  # 不可用
# proxy = '61.50.244.179:808'  # 不可用


proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

