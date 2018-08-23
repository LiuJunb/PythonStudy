import requests
import logging
from requests.packages import urllib3
# 1.忽略控制台的警告
#urllib3.disable_warnings()

# 1.通过捕获警告到日志的方式忽略警告
logging.captureWarnings(True)

# 2.不校验SSL: verify=False
resposne = requests.get('https://www.12306.cn', verify=False)
print(resposne.status_code)

