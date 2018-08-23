import re

#  ?   0 或者 1 个
#  *   0 或者 多个
#  +   1 或者多个
content = '54aK54yr5oiR54ix5L2g'


# 1.使用 +
content1 = re.sub('\d+', '', content)
print(content1)

# 2.使用 ？
content2 = re.sub('\d?', '', content)
print(content2)