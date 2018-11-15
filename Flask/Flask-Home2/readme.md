# 1.项目目录结构

Flask-Home2:

    ihome                   应用的根目录
        api_v_1_0           蓝图
            __init__.py     蓝图初始化
            index.py        定义接口

        __init__.py         定义程序的初始化

    config.py               配置文件
    manage.py               入口管理
    readme.md               说明


 # 2.搭建目录结构   


 # 3.启动redis:

    brew services start redis
    redis-server /usr/local/etc/redis.conf
    
    brew services stop redis
    brew services restart redis