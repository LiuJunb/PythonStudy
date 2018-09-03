import  requests

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

# 1.手动从代理池里面获取一个有效的代理
print(get_proxy())