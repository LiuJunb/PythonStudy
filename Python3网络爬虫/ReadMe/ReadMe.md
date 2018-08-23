#Python3网络爬虫开发实战

[《Python3网络爬虫开发实战》](https://germey.gitbooks.io/python3webspider/content/1.2.1-Requests%E7%9A%84%E5%AE%89%E8%A3%85.html)


##1.Python3

**1. python3 安装目录:**

```python
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7
```

**2. pip3 安装目录：** 

```python
/Library/Frameworks/Python.framework/Versions/3.7/lib/pip3
```


**3. 安装第三方的库一般存放在：**

```python
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages 
```


##1.pip3 



```python


```

##2.软件安装

在用户的根目录下的.bash_profile文件中配置：

```python

export PATH=$PATH:/usr/bin/phantomjs-2.1.1-macosx/bin

# Setting PATH for Python 3.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH

```

###1.PhantomJS

UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
  warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '


###2.tesserocr

安装比较久


###3.mysql 8.0.12

1.mac通过安装包安装社区版：https://dev.mysql.com/downloads/file/?id=479845

2.安装过程选择默认：root -> rootadmin
 
3.查看mysql是否启动和安装目录：mac -> 系统设置偏好 -> mysql

4.查看数据库的navcat软件

5.配置mysql的环境变量：

    //直接在终端执行（环境变量不会写到.bash_profile中）： 
    PATH="$PATH":/usr/local/mysql/bin 

6.mysql常用的命令：

```mysql
    # 1.链接数据库
    mysql -uroot -padmin
    # 2.查看和选择数据库
    SHOW  DATABASES;
    USE database_name;
    SHOW TABLES;

```

###4.mongoDB 4.0.1

1.下载地址：https://www.mongodb.com/download-center?jmp=nav#community

2.安装教程：http://www.runoob.com/mongodb/mongodb-osx-install.html

3.mongoDB 配环境变量：

    # mongodb 手动安装在： /usr/bin/mongodb 下，所以环境变量配置为：
    
    export PATH=$PATH:/usr/bin/mongodb/bin
    
    
4.检查环境变量是否配好( 默认的端口：27017 )：

    终端执行 mongod ,注意不是 mongodb ;
    mongod --help 查看帮助
      

5.创建数数据库：
    
    sudo mkdir -p /data/db   # mac电脑 mongodb 默认的数据在/data/db
 
6.启动mongodb    

    sudo mongod

6.2 关闭mongodb server

    > mongo
    > use admin
    > db.shutdownServer()

7.安装数据库可视化界面：RoboMongo/Robo 3T 1.2.1

下载页面 ： https://robomongo.org/download


8.运行Robo 3T提示（打不开“XXX”，因为它来自身份不明的开发者）：
 
解决办法：系统偏好设置>>安全与隐私>>允许安装未知来源


###5.redis 安装

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



### 6.pyspider安装和问题解决
* 问题一：pyspider不支持python3.7
    * 解决方案：修改源码
    * ![](https://note.youdao.com/yws/public/resource/2c69ccd7c071e122aada0d09d6a84867/xmlnote/30CA026AFC7B4F12A260056711AA87EF/3660)
    * ![](https://note.youdao.com/yws/public/resource/2c69ccd7c071e122aada0d09d6a84867/xmlnote/15EF37077BEF4E4EA1DCBEB504AB63EC/3662)
* 问题二：ImportError: pycurl: libcurl link-time version (7.49.1) is older than compile-time version (7.51.0)
    * 问题图片：![](https://note.youdao.com/yws/public/resource/2c69ccd7c071e122aada0d09d6a84867/xmlnote/1E83BC805A9246B082F5E83A37A5F5AC/3664)
    * 解决方案：
    ```shell
    pip3 uninstall pycurl
    
    export LD_LIBRARY_PATH=/usr/local/opt/curl/lib
    export LIBRARY_PATH=/usr/local/opt/curl/lib 
    
    export LD_LIBRARY_PATH=$(brew --prefix openssl)/lib
    export CPATH=$(brew --prefix openssl)/include
    export PKG_CONFIG_PATH=$(brew --prefix openssl)/lib/pkgconfig
    
    pip3 install pycurl
    ```
* 问题三：Error: Could not create web server listening on port 25555
    * 问题原因：需要在活动监视器中关闭phantomjs进程
    * 重新启动即可

###7.docker

下载地址 ：https://www.docker.com/products/docker-desktop

配置镜像 ： https://n2ys6llb.mirror.aliyuncs.com

###8.


brew install curlbrew install curl

##3.软件的安装
   

 


















