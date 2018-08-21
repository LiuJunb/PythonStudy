import re

content = 'Hello 1234567 World_This is a Regex Demo'

# 目标是匹配出： 1234567
result = re.match('^Hello\s(\d+)\sWorld', content)

print(result)  # <re.Match object; span=(0, 19), 01-match='Hello 1234567 World'>
print(result.group())  # Hello 1234567 World_This
print(result.group(1))  # 1234567
print(result.span())  # (0, 25)

# 我们获取用的是group(1)，与 group() 有所不同，group() 会输出完整的匹配结果，
# 而 group(1) 会输出第一个被 () 包围的匹配结果，假如正则表达式后面还有 () 包括的内容，
# 那么我们可以依次用 group(2)、group(3) 等来依次获取




