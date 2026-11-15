"""
    获取验证码
"""
#1.导库
import requests

def cap_image():
    #2.请求准备
    url = "http://kdtx-test.itheima.net/api/captchaImage"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }
    #3.发送请求
    respond = requests.get(url,headers=headers)

    #4.打印结果
    return respond.json()["uuid"]
    print(respond.json())

