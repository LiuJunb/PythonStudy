# 定义Car类
class Car:
    """一次模拟汽车的简单的尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_des_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print('汽车里程:' + str(self.odometer_reading))

    def update_odometer(self, value):
        """通过方法来修改属性的值"""
        if value >= self.odometer_reading:
            self.odometer_reading = value
        else:
            print('you can not roll back odometer')

    def increment_odometer(self, value):
        """对里程碑数的最加"""
        self.odometer_reading += value


# 定义 ElectricCar类 继承 Car类
class ElectricCar(Car):
    """定义电动车类"""
    def __init__(self, make, model, year):
        """初始化夫类中的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def get_des_battery(self):
        """获取电瓶容量的信息"""
        print('电瓶容量是：' + str(self.battery_size))
        return self.battery_size


# 创建一个台电动车
my_electric_car = ElectricCar('tesla', 'model s', 2017)
print(my_electric_car.get_des_name())

# 调用方法
my_electric_car.get_des_battery()

