# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=7Yi9ILpQdwclwP9ZZkz68aZG&client_secret=tsEdPeFxv7WFGtLEEGs28usPYAmz3pwX'
response = requests.get(host)
if response:
    print(response.json())