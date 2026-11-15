"""
    上传合同文件
"""
import requests

import config
from utils import tools


def upload_file_name():
    url = f"{config.BASE_URL}/api/common/upload"
    headers = {
        "Authorization": tools.get_token_func(),
        "User-Agent": config.BASE_User_Agent,
        # "Content-Type": "multipart/formdata"
        #注意：使用files 参数时，request 库会自动添加"Content-Type": "multipart/formdata"类型，不必再手动添加，否则会报错！
    }
    files = {
        "file": open("../data/demo.pdf", "rb")#说明：rb以二进制的方式读取
    }
    respond = requests.post(url,headers=headers,files=files)
    return respond.json().get("fileName")
