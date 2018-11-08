# coding:utf-8
from flask import Flask, request
app =Flask(__name__)

@app.route('/upload', methods = ['POST'])
def upload():
    file_obj = request.files.get('pic')
    if file_obj is None:
        # 表示没有发送文件
        return '没有上传文件'
 
    # 将上传的文件保存到本地
    # 1.创建一个文件
    f = open('./demo.png', 'wb')
    # 2.向文件写内容
    data = file_obj.read()
    f.write(data)
    # 3.关闭文件
    f.close()
    
    return '上传成功'


@app.route('/upload2', methods = ['POST'])
def upload2():
    file_obj = request.files.get('pic')
    if file_obj is None:
        # 表示没有发送文件
        return '没有上传文件'
 
    # 将上传的文件保存到本地
    # 1.创建一个文件
    with open('./demo.png', 'wb') as f:
        # 2.向文件写内容
        data = file_obj.read()
        f.write(data)
        
    return '上传成功'


def index():
    pass 
def main():
    app.run(debug = True)


if __name__ == '__main__':
    main()    
