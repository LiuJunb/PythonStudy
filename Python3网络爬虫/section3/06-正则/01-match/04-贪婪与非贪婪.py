import re
#  .*? （点星） 可以匹配任意字符（除换行符,例如节点会有换行）
#  .?  （点）  可以匹配任意字符（除换行符）
#  *  （星）  又代表匹配前面的字符无限次
content = 'Hello 1234567 World_This is a Regex Demo'

# 1.贪婪匹配（.*）尽量匹配最多的字符： ^He .*  (\d+) .*  Demo$
result = re.match('^He.*(\d+).*Demo$', content)
print(result)  # <re.Match object; span=(0, 40), 01-match='Hello 1234567 World_This is a Regex Demo'>
print(result.group(1))  # 7


# 2.非贪婪匹配（.*？）尽量匹配最少的字符,例如在尾部时可以一个都不匹配： ^He .*?  (\d+) .*  Demo$
result2 = re.match('^He.*?(\d+).*Demo$', content)
print(result2)  # <re.Match object; span=(0, 40), 01-match='Hello 1234567 World_This is a Regex Demo'>
print(result2.group(1))  # 1234567


# 今天天气和好[haha],适合敲代码[xixi]

# '\[ .* \]'   -->  [haha],适合敲代码[xixi]
# '\[ .*? \]'   --> [haha]




