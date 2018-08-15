# 1.创建Dog类
class Dog:

    # 1.1默认的构造函数（ ———init———）
    def __init__(self, name, age):
        """初始化属性name 和 age """
        self.name = name
        self.age = age

    # 1.2自定义方法
    def sit(self):
        """小狗蹲下"""
        print(self.name.title() + ' 蹲下')


my_dog = Dog('jack', 2)
print(my_dog)  # <__main__.Dog object at 0x104fe34a8>

# 访问属性
print(my_dog.name)  # jack
print(my_dog.age)  # 2

# 调用方法
my_dog.sit()  # Jack 蹲下







