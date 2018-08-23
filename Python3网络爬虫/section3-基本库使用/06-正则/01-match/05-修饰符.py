import re

# 定义一个字符串模版
content = '''Hello 1234567 World_This
is a Regex Demo
'''

# 添加匹配-换行的修饰符(re.S)：  ^He .*? (\d+) .*? Demo$
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group())
print(result.group(1))  # 1234567








