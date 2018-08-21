import requests

from requests.packages import urllib3
# 1.忽略控制台的警告
urllib3.disable_warnings()

# 2.不校验SSL: verify=False
# 我们需要有 crt 和 key 文件，指定它们的路径。注意本地私有证书的 key 必须要是解密状态，加密状态的 key 是不支持的
resposne = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(resposne.status_code)

