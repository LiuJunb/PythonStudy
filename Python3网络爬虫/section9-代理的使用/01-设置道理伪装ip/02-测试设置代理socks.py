# http://www.xicidaili.com/
# 西刺免费代理
from urllib.error import  URLError
from urllib import request
import socks
import socket

PORT = 6666
# 这里的代码没有测试通
proxy = '121.31.103.33'  # 6666 可用socks4/5
# proxy = '110.73.33.207'  # 6673 可用 socks4/5

# proxy = '110.73.30.246'  # 6666 不可用socks4/5
# proxy = '171.38.64.67'  # 6675不可用socks4/5
# proxy = '110.73.32.7'  # 6666 不可用socks4/5

socks.set_default_proxy(socket.SOCK_SEQPACKET, proxy, PORT)
# socks.set_default_proxy(socket.SOCK_STREAM, proxy, PORT)
socket.socket = socks.socksocket

try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

