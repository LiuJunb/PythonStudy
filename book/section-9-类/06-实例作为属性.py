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


# 定义 Battery 类
class Battery:
    """定一个描述电池的类"""
    def __init__(self, battery_size=70):
        """初始化 Battery 类的属性"""
        self.battery_size = battery_size

    def des_battery(self):
        """获取电瓶信息的方法"""
        print(' this car has a battery : ' + str(self.battery_size))


# 定义 ElectricCar类 继承 Car类
class ElectricCar(Car):
    """定义电动车类"""
    def __init__(self, make, model, year):
        """初始化夫类中的属性"""
        super().__init__(make, model, year)
        """新建一个 Battery 实例来作为该类的属性"""
        self.battery_size = Battery()

    def get_des_battery(self):
        """获取电瓶容量的信息"""
        self.battery_size.des_battery()

    def read_odometer(self):
        """重写父亲中-打印一条指出汽车里程的信息"""
        print('电动汽车的里程:' + str(self.odometer_reading))


# 创建一个台电动车
my_electric_car = ElectricCar('tesla', 'model s', 2017)
print(my_electric_car.get_des_name())

my_electric_car.update_odometer(40)
# 调用方法
my_electric_car.read_odometer()

# 获取电瓶量
my_electric_car.get_des_battery()
