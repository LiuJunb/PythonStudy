from redis import StrictRedis, ConnectionPool

url = 'redis://@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

redis.set('gender', 'male')

print(redis.get('gender'))
print(redis.get('age'))
print(redis.get('name2'))  # None




