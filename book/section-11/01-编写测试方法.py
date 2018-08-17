# 1.导入测试类
import unittest
from module.user import get_full_name
# print(get_full_name('liu', 'jun'))

def get_full_name2(first_name, last_name):
    return first_name + last_name

# 2.编写测试类
class UserTestCase(unittest.TestCase):
    # 3.编写测试方法
    def test1_get_full_name(self):
        # 4.要测试的方法
        full_name = get_full_name('liu', 'jun')
        # 5.开始测试
        self.assertEqual(full_name, 'liujun')

    # 3.编写测试方法
    def test2_get_full_name2(self):
        # 4.要测试的方法
        full_name = get_full_name2('jack', 'jack')
        # 5.开始测试
        self.assertEqual(full_name, 'jackjack')


# 5.让python运行这个测试文件
unittest.main()
