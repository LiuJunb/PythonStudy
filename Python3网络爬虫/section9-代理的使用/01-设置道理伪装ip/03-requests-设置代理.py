import requests

proxy = '120.24.152.123:3128'  # 可用https
# proxy = '111.155.116.234:8123'  # 可用 http


# proxy = '111.155.116.221:8123'  # 不可用
# proxy = '111.155.116.236:8123'  # 不可用
# proxy = '61.50.244.179:808'  # 不可用

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)















