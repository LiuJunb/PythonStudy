from redis import StrictRedis
from random import choice
from setting import REDIS_HOST, REDIS_PORT, REDIS_KEY, MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from poolemptyerror import PoolEmptyError


class RedisClient:

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=None):
        """初始化"""
        self.db = StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """给REDIS_KEY添加代理"""
        if not self.db.zscore(REDIS_KEY, proxy):  # 判断key是否存在
            return self.db.zadd(REDIS_KEY, score, proxy)  # 如果key不存在就添加

    def random(self):
        """随机获取有效代理，尝试获取最高分代理，如果最高分数不存在，则按照排名获取，否则异常"""
        # 尝试获取最高分代理
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)  # 获取key在 MAX_SCORE 和 MAX_SCORE 之间
        if len(result):
            # 返回列表中的一个随之值
            return choice(result)
        else:
            # 按照排名获取（排名默认是按照分数高的在前面，依次冲排名第1查找到排名100）
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                # 抛出自定义异常
                raise PoolEmptyError

    def decrease(self, proxy):
        """代理值减一分，分数小于最小值，则代理删除"""
        # 判断这个key中的proxt是否存在，如果存在返回分数
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理,', proxy, '当前分数', score, '减一')
            return self.db.zincrby(REDIS_KEY, proxy, -1)   # 分数减一
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)  # 删除

    def exists(self, proxy):
        """判断某个代理是否存在"""
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """将代理设置为最大值"""
        print('代理,', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """获取数量"""
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """获取全部代理"""
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)











