import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'

# compile() 方法可以说是给正则表达式做了一层封装。
# compile() 还可以传入修饰符，例如 re.S 等修饰符，这样在 search()、findall() 等方法中就不需要额外传了
pattern = re.compile('\d{2}:\d{2}')

rex = '\d{4}-\d{2}-\d{2}\s'

result1 = re.sub(rex, '', content1)
# 把 12:00 替换为空格
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)

print(result1, result2, result3, sep='\n')




