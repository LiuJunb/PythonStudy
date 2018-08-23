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


my_new_car = Car('bao mao', 'a4', 2017)
print(my_new_car.get_des_name())

# 直接修改属性的值
my_new_car.odometer_reading = 25
my_new_car.read_odometer()

# 通过方法来修改属性的值
my_new_car.update_odometer(50)
my_new_car.read_odometer()

