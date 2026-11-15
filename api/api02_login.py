"""
    登录
"""
#1.导库
import requests
import config
from api.api01_cap_image import cap_image

#2.请求准备
def login(username, password,code):
    uuid = cap_image()
    url = config.BASE_URL+"/api/login"
    headers = {
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }
    jsons = {
        "username": username,
        "password": password,
        "code": code,
        "uuid":uuid
    }
        #3.发送请求
    respond = requests.post(url =url,headers=headers,json=jsons)
        #4.打印结果
    return respond
