# coding:utf-8
import unittest
from main import app
import json

class TestViewsClass(unittest.TestCase):

    def setUp(self):
        """在测试进行之前，先被执行"""
        # 设flask工作在测试模式下，这样如果接口代码有错返回500，测试控制台可以查看错误信息
        app.config['TESTING'] = True
        # app.testing = True
        
        self.client = app.test_client()

    def test_empty_username_and_password(self):

        # 1.获取请求对象
        # client = app.test_client()
        # 2.发起一个post请求
        ret = self.client.post('/', data={})
        # 3.获取到结果
        result = ret.data
        # print(result)
        # 4.把json字符串 转成 json对象
        resp = json.loads(result)
        # print(resp)
        
        # 5.断言测试
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 1)
        
        # 6.还可继续编写测试，例如重复第二步

if __name__ == '__main__':
    # 6.运行所有的测试类中所有的函数
    unittest.main()