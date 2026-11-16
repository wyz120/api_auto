"""
    模块：合同管理
"""
import os
import random
import requests
from config import config
from common import tools
from config.config import BASE_File_Path


class ApiContract():
    #合同文件名称
    file_name = None
    #接口1：合同上传
    def upload_file_name(self):
        url = f"{config.BASE_URL}/api/common/upload"
        headers = {
            "Authorization": tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent,
            # "Content-Type": "multipart/formdata"
            #注意：使用files 参数时，request 库会自动添加"Content-Type": "multipart/formdata"类型，不必再手动添加，否则会报错！
        }

        file_path = os.path.join(config.BASE_DIR, "data/","demo.pdf")
        files = {
            "file": open(file_path, "rb")#说明：rb以二进制的方式读取
        }
        respond = requests.post(url,headers=headers,files=files)
        ApiContract.file_name = respond.json().get("fileName")
        return respond

    #接口2：新增合同
    def add_contract(self,name,phone,subject):
        url = f"{config.BASE_URL}/api/contract"
        headers = {
            'Authorization': f'{tools.get_token_func()}',
            "User-Agent": f'{config.BASE_User_Agent}',
            'Content-Type': 'application/json'
        }
        json = {
            "name": name,
            "phone": phone,
            "contractNo": f"HT10{random.randint(100000, 999999)}",
            "subject": subject,
            "courseId": 62830,
            "channel": "0",
            "activityId": "",
            "fileName": f"{ApiContract.file_name}"
        }
        respond = requests.post(url, headers=headers, json=json)
        return respond
    #接口3：查询合同列表
    def query_contract_list(self,phone):
        url = f"{config.BASE_URL}/api/contract/list?phone={phone}"
        headers = {
            'Authorization': f'{tools.get_token_func()}',
            "User-Agent": f'{config.BASE_User_Agent}',
            'Content-Type': 'application/json'
        }
        respond = requests.get(url, headers=headers)
        return respond
    #接口4：删除合同
    def delete_contract(self,id):
        url = f"{config.BASE_URL}/api/contract/remove?id={id}"
        headers = {
            'Authorization': tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent,
            'Content-Type': 'application/x-www-formurlencoded'
        }
        respond = requests.post(url, headers=headers)
        return respond
