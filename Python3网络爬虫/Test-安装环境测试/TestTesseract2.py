import os

from PIL import Image
from pytesseract import image_to_string
import pytesseract

# 设置tesseract命令行的位置
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/3.05.02/bin/tesseract'
# http://my.cnki.net/elibregister/commonRegister.aspx

def verify_yzm(filename):
    f1, f2 = os.path.splitext(filename)

    calc_result = None
    try:
        im = Image.open(filename)

        # 1.切掉四周的黑边
        width = im.size[0]
        height = im.size[1]
        left = 4
        top = 4
        right = width - 4
        bottom = height - 4
        box = (int(left), int(top), int(right), int(bottom))
        im = im.crop(box)
        im = im.resize((width * 4, height * 4), Image.BILINEAR)
        im.save(f1 + '_step1' + f2)

        # 2.转为灰度图（转为灰度图才能二值化-去噪）
        imgry = im.convert('L')
        imgry.save(f1 + '_step2' + f2)

        # 3.去噪( 去除干扰的线条, 使整个验证码变的黑白分明 )
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        out.save(f1 + '_step3' + f2)

        # 调用
        text = image_to_string(out, config='-l eng')
        print('text: ', text)

    except Exception as e:
        print(e)
    return calc_result


if __name__ == '__main__':
    verify_yzm('image2.jpeg')