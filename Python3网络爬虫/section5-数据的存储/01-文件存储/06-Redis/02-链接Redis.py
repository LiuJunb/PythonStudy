from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379)

redis = StrictRedis(connection_pool=pool)

redis.set('age', 20)

print(redis.get('age'))