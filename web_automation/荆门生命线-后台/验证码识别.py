# 作者
# NATURE
# 日期
# 2022/11/22 15:19
# 功能
#
from PIL import Image
from selenium import webdriver
import requests
import pytesseract


# 获取图片
def get_img(img_path):
    img = Image.open(img_path)
    return img


# 对图片进行灰度处理
def image_grayscale_deal(image):
    img = image.convert("L")
    image.show()
    return img


# 对图片进行二值化处理
def image_threashoding_method(image):
    threshold = 70
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, "1")
    image.show()
    return image


# 图像识别
def captcha_crack(image):
    result = pytesseract.image_to_string(image)
    return result


image = get_img('./picture/yzm.png')
image = image_grayscale_deal(image)
image = image_threashoding_method(image)
print(captcha_crack(image))
