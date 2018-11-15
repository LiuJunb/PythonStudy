# 1.项目目录结构
Flask-Home2:

    ihome                   应用的根目录
        api_v_1_0           蓝图
            __init__.py     蓝图初始化
            index.py        定义接口

        __init__.py         定义程序的初始化

        web_html            静态资源的蓝图
            __init__.py     蓝图初始化

    config.py               配置文件
    manage.py               入口管理
    readme.md               说明

 # 2.集成 数据库

 models.py 一定要被项目引入

# 3. 集成静态资源

    static


# 4.定义静态资源的蓝图

    web_html

# 5.自定义re转换器

# 6.csrf 防护

    前端发送post请求需要：cookie ： csrf_token=xx ; body : csrf_token=xx