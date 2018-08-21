import requests

# 1.下载图片
r = requests.get('https://github.com/favicon.ico')

print(type(r))  # <class 'requests.models.Response'>
print(r.text)   # 字符窜
print()
print(r.content)  # bytes

# 2.保存图片
with open('favicon.ico', 'wb') as f:
    f.write(r.content)






