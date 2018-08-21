import requests

# 3.设置cookie的封装
_cookies_ = '_zap=2f6bd876-c06d-475d-aa25-8ea9201cc02b; d_c0="APAk_ZdJDA6PTvHs1JIN9veBeU3n1SmoSTc=|1534122767"; q_c1=7e1bc55cafa7428d8444b025ed795a44|1534122770000|1534122770000; l_cap_id="YmNkNGFjZTljYjJjNDkyNjlkOTEzMzZiNTViMmYzMWM=|1534125485|6558e5ab52a67bd455b5cef90ffe6c80481ef3aa"; r_cap_id="ODg0NTlmMTY3ZTI3NGRhNDk5Mjg4NWI0ZWY5ZGM5YWM=|1534125485|3aa46dd799e1b1a3aa1b709a7151da7fac39dea6"; cap_id="MDFkNGZjNzRkY2JhNDk1ZGE3OWZlYWM3YWQ0ZTQzZDk=|1534125485|028d46570389647bce5304749970a83f84674c83"; _xsrf=ff2e87c1-2040-40d9-9f6b-f7b6a1e7aa68; tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; capsion_ticket="2|1:0|10:1534758623|14:capsion_ticket|44:ODE5Nzc0ZmM2Mjc2NDViY2I0ZTA5ZjE2NzM5ZmNiZjg=|afac89ede21fc47e8542a7a2b4baba2096586f780235dc91c39aba2f159c62d9"'

jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3489.1 Safari/537.36'
}

# 使用 RequestsCookieJar 提供cookie
for cookie in _cookies_.split(';'):
    # print(cookie)
    # print(type(cookie.split('=', 1)))  # <class 'list'>
    key, value = cookie.split('=', 1)  # 数列的解构, 遇见第一个=号打断
    # print(key, value)
    jar.set(key, value)

r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)












