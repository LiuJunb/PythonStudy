import sys
from scrapy.utils.project import get_project_settings
from scrapyuinversal.spiders.universal import UniversalSpider
from scrapyuinversal.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():
    # china
    name = sys.argv[1]
    custom_settings = get_config(name)

    # 爬虫使用的Spider名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()  # 获取项目中默认的配置settings.py
    settings = dict(project_settings.copy())

    # 合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)  # 开始一个爬虫进程

    # 启动universal爬虫进程（并传递参数过universal.py）
    process.crawl(spider, **{'name': name})  # scrapy crawl universal
    process.start()


if __name__ == '__main__':
    run()