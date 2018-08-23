from redis import StrictRedis

# 默认不传的情况下，这四个参数分别为 localhost、6379、0、None
redis = StrictRedis(host='localhost', port=6379)

# 1.读取数据
print(redis.get('name'))

# 2.判断一个key是否存在
print(redis.exists('name'))

# 3.删除一个key
print(redis.delete('name'))
print(redis.exists('name'))

# 4.判断一个key的类型
print(redis.type('age'))

print('==========5==========')
# 5.获取所有符合规则的keys
print(redis.exists('gender'))
pattern = 'g*'
print(redis.keys(pattern))