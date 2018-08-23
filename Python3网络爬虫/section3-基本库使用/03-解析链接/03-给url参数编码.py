from urllib.parse import urlencode, parse_qs, quote

# 字典类型
params = {
    'name': '刘军',
    'age': 22
}
base_url = 'http://www.baidu.com?'

# 1.给url中的参数编码
url = base_url + urlencode(params)
print(url)  # http://www.baidu.com?name=%E5%88%98%E5%86%9B&age=22


# 2.对参数解码 parse_qs() 返回字典  parse_qsl() 返回元组
query = 'name=%E5%88%98%E5%86%9B&age=25'
print(parse_qs(query))  # {'name': ['刘军'], 'age': ['25']}  字典类型


# 3.对内容进行编码 quote()
name = '刘'
print('http://www.baidu.com?name='+quote(name))  # http://www.baidu.com?name=%E5%88%98







