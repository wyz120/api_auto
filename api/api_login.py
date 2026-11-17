"""
    模块：登录
"""
#1.导库
import requests
import config
from config import config

#2.请求准备
class ApiLogin():
    #1.获取验证码
    def cap_image(self):
        # 2.请求准备
        url = config.BASE_URL + "/api/captchaImage"
        headers = {
            "User-Agent": config.BASE_User_Agent
        }
        # 3.发送请求
        respond = requests.get(url, headers=headers)

        # 4.打印结果
        return respond.json()["uuid"]


    #2.登录接口
    def api_login(self,username, password,code):
        uuid = ApiLogin().cap_image()
        url = config.BASE_URL+"/api/login"
        headers = {
            "content-type": "application/json",
            "User-Agent": config.BASE_User_Agent
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
