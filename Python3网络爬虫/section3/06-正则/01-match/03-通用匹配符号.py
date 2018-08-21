import re
#  .* （点星） 可以匹配任意字符（除换行符,例如节点会有换行）
#  .  （点）  可以匹配任意字符（除换行符）
#  *  （星）  又代表匹配前面的字符无限次
content = 'Hello 123 4567 World_This is a Regex Demo'

# 目标是匹配出：Hello 123 4567 World_This is a Regex Demo
# ^Hello  .*   Demo$
result = re.match('^Hello.*Demo$', content)

print(result)  # <re.Match object; span=(0, 41), 01-match='Hello 123 4567 World_This is a Regex Demo'>
print(result.group())  # Hello 123 4567 World_This is a Regex Demo
print(result.span())  # (0, 41)





