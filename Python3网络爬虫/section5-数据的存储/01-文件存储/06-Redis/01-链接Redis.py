from redis import StrictRedis

# 默认不传的情况下，这四个参数分别为 localhost、6379、0、None
redis = StrictRedis(host='localhost', port=6379)

# 1.存数据
# redis.set('name', 'Bob1')
# redis.set('name', 'Bob2')
# 2.读取数据
print(redis.get('name'))
print(redis.get('set'))
print(redis.get('hash'))
print(redis.get('list'))