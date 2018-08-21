import requests

files = {'file': open('favicon.ico', 'rb')}

# post 提交文件 files=
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
