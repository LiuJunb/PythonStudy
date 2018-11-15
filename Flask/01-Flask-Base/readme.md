# 1.创建虚拟环境：

https://www.jianshu.com/p/08c657bd34f1

# 2.vscode 搭建python环境

https://www.jianshu.com/p/506debe61423

# 3.vscode 链接python的虚拟环境

修改setting.json 配置文件。 "python.pythonPath": "/Users/android-school/Python/myPython2Env/bin/python"

https://code.visualstudio.com/docs/python/environments

https://stackoverflow.com/questions/37642045/use-virtualenv-with-python-with-visual-studio-code-in-ubuntu


# 4.python 2 安装flask-mysqldb 错误

Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/4f/hz1dtvlx3jb0_x9r4w2zfqch0000gq/T/pip-install-sVjSMD/mysqlclient/

https://github.com/admiralobvious/flask-mysqldb


###5.redis 安装(默认端口：6379)

http://www.runoob.com/redis/redis-install.html

1.使用brew安装:

    brew install redis

2.默认的安装路径：
    
3.默认的配置文件路径：

    /usr/local/etc/redis.conf

4.启动redis:

    brew services start redis
    redis-server /usr/local/etc/redis.conf
    
    brew services stop redis
    brew services restart redis















# python2 vs python3 语法区别

1）# coding:utf-8
2) super(ClassName,self).__init__(xxx,xxx)
3) python 2 中类的继承必须要指定, python3就不用
4）python 2 字符串
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819196283586a37629844456ca7e5a7faa9b94ee8000
    str 'ascii'
    unicode

        --> utf-8 -->一般用在指定文件存储的格式

    eg:

    a = '中国'   # str
    a= u'中国'   # unicode

python 3 字符串

    unicode 

        --> utf-8 -->

5） 

python 2 异常处理

try:
    raise
except Exception, e:
    print (e)
    return false
    python 2 异常处理

python3 异常处理
try:
    raise
except Exception as e:
    print (e)
    return false


6) map()
map 函数 在python2 中返回是具体的值
map 函数 在python3 中返回是对象, 可以通过list拿到具体的值












