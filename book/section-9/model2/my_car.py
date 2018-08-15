# 导入外部的模块
# from model2.car import Car, Battery, ElectricCar
# from model2.car import *


# my_new_car1 = Car('bao ma1', 'a4', 2018)
# my_new_car2 = ElectricCar('bao ma2', 'a4', 2018)
# print(my_new_car1.get_des_name())
# print(my_new_car2.get_des_name())


import model2.car as car

my_new_car1 = car.Car('bao ma1', 'a4', 2018)
my_new_car2 = car.ElectricCar('bao ma2', 'a4', 2018)
print(my_new_car1.get_des_name())
print(my_new_car2.get_des_name())







