"""
    登录
"""
#1.导库
import requests

import config
from api01_cap_image import cap_image
from config import BASE_URL


#2.请求准备
def login():
    uuid = cap_image()
    url = config.BASE_URL+"/api/login"
    headers = {
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }
    jsons = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid":uuid
    }
    #3.发送请求
    respond = requests.post(url =url,headers=headers,json=jsons)
    #4.打印结果
    return respond.json()["token"]
    print(respond.status_code)
    print(respond.json())