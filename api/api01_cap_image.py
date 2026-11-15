"""
    获取验证码
"""
#1.导库
import requests

import config


def cap_image():
    #2.请求准备
    url = config.BASE_URL+"/api/captchaImage"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }
    #3.发送请求
    respond = requests.get(url,headers=headers)

    #4.打印结果
    return respond.json()["uuid"]
    print(respond.status_code)
    print(respond.json())
