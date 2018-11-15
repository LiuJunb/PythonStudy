# coding:utf-8

from celery import Celery
from ihome.libs.yuntongxun.sms import CCP


# 1.定义celery对象
celery_app = Celery("ihome", broker="redis://127.0.0.1:6379/1")

# 2.定义一个任务
@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)

#3.调用/发布任务（ 把这个函数引入后可以调用 ）
# send_sms.delay(to, datas, temp_id)


# 4.celery开启worker的命令（ 与flask启动的目录一样 ）
# celery -A ihome.tasks.task_sms worker -l info
