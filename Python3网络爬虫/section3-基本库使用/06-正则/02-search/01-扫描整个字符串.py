#   search()，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

# 1.使用match
result1 = re.match('Hello.*?(\d+).*?Demo', content)
print(result1)  # None


# 2.使用search:  Hello .*? (\d+) .*? Demo
result2 = re.search('Hello.*?(\d+).*?Demo', content)
print(result2)  # <re.Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>
print(result2.group(1))  # 1234567




