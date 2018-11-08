# coding:utf-8
from flask import Flask, render_template
from flask_mail import Mail, Message
app = Flask(__name__)

# 通过开启QQ邮箱SMTP服务设置.
# 配置邮件：服务器／端口／传输层安全协议／邮箱名／密码(授权码)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '1552752805@qq.com',
    MAIL_PASSWORD = 'asotlecpmyfbjiic',
)

mail = Mail(app)

@app.route('/')
def index():
    # sender 发送方，recipients 接收方列表
    msg = Message("This is a test ",sender='1552752805@qq.com', recipients=['liujun@520it.com'])
    #邮件内容
    msg.body = "Flask test mail"
    #发送邮件
    mail.send(msg)

    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 