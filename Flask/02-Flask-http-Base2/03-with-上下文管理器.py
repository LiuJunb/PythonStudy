# coding:utf-8
# with open()  as f: 关闭文件的原理
class Foo(object):

    def __enter__(self):
        """进入with"""
        print('enter caller')
        print(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with"""    
        print(exc_type,'leave 1') 
        print(exc_val,'leave 2')
        print(exc_tb,'leave 3')

with Foo() as f:
     print('foo content')
     1 / 0




        
    


         
        