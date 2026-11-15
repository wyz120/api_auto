"""
新增课程
"""
import requests
import config
from utils import tools


def add_course(name,subject,price,applicablePerson,info):
    url = config.BASE_URL+"/api/clues/course"
    headers = {
        "Authorization": tools.get_token_func(),
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }
    jsons = {
        "name": name,
        "subject": subject,
        "price": price,
        "applicablePerson": applicablePerson,
        "info": info
    }

    response = requests.post(url,headers=headers,json=jsons)
    return response
