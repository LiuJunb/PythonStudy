import requests

proxies = {
    'http': 'http://127.0.0.1:51599',
    'https': 'https://127.0.0.1:51599'
}

# 如果本地的51599 这个端口没有实现代理的功能会报错：requests.exceptions.ProxyError: HTTPConnectionPool
# 解决方案：在本地开始一个代理服务监听51599这端口
res = requests.get('http://httpbin.org/get', proxies=proxies)
print(res.status_code)
print(res.text)

#  requests.get('http://httpbin.org/get', proxies=proxies) -> http://127.0.0.1:51599  -> http://httpbin.org/get
#  http://httpbin.org/get --> http://127.0.0.1:51599 --> res
