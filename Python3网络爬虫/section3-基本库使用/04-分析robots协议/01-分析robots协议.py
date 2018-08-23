from urllib.robotparser import RobotFileParser
from urllib.error import URLError
import ssl
# 第一种方案解决 ssl验证的问题
# from robatparserexp import RobotFileParserExp
# rp = RobotFileParserExp()

# 第二种配置全局的 不验证ssl
ssl.create_default_context = ssl._create_unverified_context
rp = RobotFileParser()

rp.set_url('http://www.jianshu.com/robots.txt')

# 执行rp.read报错
try:
    rp.read()  # 01-发起网络请求
except URLError as e:
    print(e, sep='\n')

# 判断 http://www.jianshu.com/p/b67554025d7d 这个网站是否可以爬取
print(rp.can_fetch('*', 'https://www.jianshu.com/p/4ef8ae3c912c'))  # False
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))  # False

print(rp.can_fetch('YisouSpider', 'https://www.jianshu.com/p/4ef8ae3c912c'))  # False
print(rp.can_fetch('YisouSpider', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))  # False
