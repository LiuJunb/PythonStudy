import requests

data = {
    'name': 'jack',
    'age': 20
}

# post 方法是data= ; get 方法是params=
r = requests.post('https://httpbin.org/post', data=data)
print(requests.codes.ok)  # Requests 还提供了一个内置的 Status Code 查询对象
print(requests.codes.not_found)  # 404
print('====================')
print(r.status_code, r.headers, r.cookies, r.url, r.history, sep='\n')
print(r.text)