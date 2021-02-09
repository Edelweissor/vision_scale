from aip import AipImageClassify
import requests
import base64

""" 你的 APPID AK SK """
APP_ID = '23411439'
API_KEY = '7Yi9ILpQdwclwP9ZZkz68aZG'
SECRET_KEY = 'tsEdPeFxv7WFGtLEEGs28usPYAmz3pwX'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# encoding:utf-8
'''
细粒度图像识别
'''
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
# 二进制方式打开图片文件
f = open(r'E:\PycharmProjects\Engineering innovation design\fruit1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = '24.c9ecd19211055b58ed9e8da3c3849146.2592000.1614837776.282335-23411439'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
