# 1.定义一个函数（ 有两个形参 ）
def get_animal(animal_name, animal_type):
    """获取动画的姓名和类型"""
    print('name: '+animal_name + ' --> type: ' + animal_type)


get_animal('🐱', 'animal')  # 传递两个实参
get_animal('animal', '🐱')  # 传递两个实参


# 2.关键字实参( 避免参数顺序传递异常 )
# get_animal()  #get_animal() missing 2 required positional arguments: 'animal_name' and 'animal_type'
get_animal(animal_type='animal', animal_name='🐶')
get_animal(animal_name='🐷', animal_type='animal')


# 3.参数的默认值
def get_animal_info(animal_name='🐒', animal_type='animal'):
    """获取动画的姓名和类型"""
    print('name: '+animal_name + ' --> type: ' + animal_type)


print('---------------')
get_animal_info()
get_animal_info('🐭')
get_animal_info(animal_type='Animal')



