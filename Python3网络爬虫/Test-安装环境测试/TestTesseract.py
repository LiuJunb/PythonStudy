import pytesseract
# 系统api
from PIL import Image
image = Image.open('image.png')
print(pytesseract.image_to_string(image))

# or

# import tesserocr
# print(tesserocr.file_to_text('image.png'))








