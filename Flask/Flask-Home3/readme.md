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

 # 2.集成 flask_script  和 logs

```
    # 配置日志信息
    # 设置日志的记录等级( INFO会把 info warn erro 记录在文件中 )
    logging.basicConfig(level=logging.INFO)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小100M、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日记录器
    logging.getLogger().addHandler(file_log_handler)

    # 使用案例：logging.debug('')  logging.info('')  logging.warn('warn')  logging.error('error')  会写到logs文件中
    # import logging
    # from flask import current_app
    # current_app.logger.info('') 

```


