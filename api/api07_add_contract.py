"""
新增合同
"""
import random
import requests
from api import api06_upload_file
import config
from utils import tools

url = f"{config.BASE_URL}/api/contract"
headers = {
    'Authorization': f'{tools.get_token_func()}',
    "User-Agent": f'{config.BASE_User_Agent}',
    'Content-Type': 'application/json'
}
json = {
    "name": "账号三",
    "phone": "16669010818",
    "contractNo": f"HT10{random.randint(100000,999999)}",
    "subject": "6",
    "courseId": 62830,
    "channel": "0",
    "activityId": "",
    "fileName": f"{api06_upload_file.upload_file_name()}"
}
respond = requests.post(url,headers=headers,json=json)
print(respond.json())