from requests import Session
from config import *
from redisqueue import RedisQueue
from mysql import MySQL
from weixinrequest import WeixinRequest
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from requests import ReadTimeout, ConnectionError


class Spider():
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = 'NBA'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'CXID=300E866F4542ED22AE87B0EAAC93DE49; SUID=DE19F93A4B238B0A5B45763600018391; ABTEST=7|1535183484|v1; IPLOC=CN4401; weixinIndexVisited=1; SUV=002D1DEC1B2F3AEE5B810A7E9992A029; sct=1; JSESSIONID=aaalrUYv_EZgp9x02tBvw; PHPSESSID=1l812rviclinat3jkguqd8h4k5; SUIR=3DE9FCC8D3D1A7E910541485D4DA05AF; SNUID=C10A1F2B30355B0E7FDD6C8430137DAF; seccodeRight=success; successCount=1|Sat, 25 Aug 2018 08:36:18 GMT',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    mysql = MySQL()

    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        #  print(start_url)  # http://weixin.sogou.com/weixin?query=NBA&type=2
        # 调度第一个请求( 网页 )
        self.queue.add(weixin_request)

    # callback 函数
    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response.text)
        # 拿到item中的title
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            # title 是a 标签
            url = item.attr('href')
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    # 请求的回调
    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'date': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data

    # 发起网络请求
    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        # try:
        if weixin_request.need_proxy:
            proxy = self.get_proxy()
            if proxy:
                proxies = {
                    'http': 'http://' + proxy,
                    'https': 'https://' + proxy
                }
                return self.session.send(weixin_request.prepare(),
                                         timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)
        return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
    # except (ConnectionError, ReadTimeout) as e:
    #     print(e.args)
    #     return False


    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)


    # 调度请求
    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            # callback有两种情况
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            # 发起网络请求（每次都会修改代理）
            response = self.request(weixin_request)
            print('response ===: ', response)
            if response and response.status_code in VALID_STATUSES:
                # https://mp.weixin.qq.com/s?src=11&timestamp=1535185884&ver=1081&signature=es5CzC0VNUqdPKGjOndCHZF9*9lta4Z4SCyS9V0IzD9aHF9ruvINszh-1xqfZ4YmVqDIl9KxQacmv3KmJyXz*Aby5hVGKgaWbPt6buCTNxZeuokt7OhireVn*BJy*89Y&new=1
                # 1.results 是给生成器函数：里面有很多的 weixin_request , 获取每一个item 的detail
                # 2.results 是一个字典
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, WeixinRequest):
                            # 把请求添加多请求队列
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

            # 只执行一次
            break


    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
