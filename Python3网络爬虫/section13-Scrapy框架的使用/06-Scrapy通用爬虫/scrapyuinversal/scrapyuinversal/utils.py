from os.path import realpath, dirname
import json


def get_config(name):
    # dirname(realpath(__file__)) ==> /Users/xxxx/xxxx/xxxx/06-Scrapy通xx/scrapyuinversal/scrapyuinversal'
    path = dirname(realpath(__file__)) + '/config/' + name + '.json'
    # path = './scrapyuinversal/config/' + name + '.json'
    print('=============get_config================')
    print(path)
    with open(path, 'r', encoding='utf-8') as f:
        # print(type(f.read()))   # str
        # return json.loads(f.read())
        return json.load(f)
