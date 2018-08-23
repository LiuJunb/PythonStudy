# 在前面介绍 Urllib 时我们可以将 Request 表示为一个数据结构，
# Request 的各个参数都可以通过一个 Request 对象来表示
from requests import Request, Session

url = 'http://httpbin.org/post'

data = {
    'name': 'germey'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# 1.保存在一个会话中
s = Session()
# 2.构建一个Request数据结构
req = Request('POST', url, data=data, headers=headers)
# 3.准备好了Request
prepped = s.prepare_request(req)
# 4.开始发起网络请求，获取到结果
# send(self, request, **kwargs)
r = s.send(prepped)
print(r.text)



