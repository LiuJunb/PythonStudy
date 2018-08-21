import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))  # 41

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)

print(result)  # <re.Match object; span=(0, 25), 01-match='Hello 123 4567 World_This'>
print(result.group())  # Hello 123 4567 World_This
print(result.span())  # (0, 25)

