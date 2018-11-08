# coding:utf-8
import unittest
from connect_mysql import Role , db, app

class TestMySqlClass(unittest.TestCase):

    def setUp(self):
        # 1.配置数据库的连接
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootadmin@127.0.0.1:3306/db_flask'
        # 2.新建数据库操作对象 db（已导入）
        # 3.创建表 Role（已导入）
        # 4.执行创建表的语句
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()    


    def test_add_author(self):
        """测试添加 角色 的操作"""
        role = Role(name='admin')
        db.session.add(role)
        db.session.commit()


def main():
    unittest.main()

if __name__ == '__main__':
    main()