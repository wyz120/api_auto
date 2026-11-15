"""
新增课程
"""
import requests

import config

def add_course():
    url = config.BASE_URL+"/api/clues/course"
    headers = config.BASE_HEADERS
    jsons = {
        "name": "11月15日软件测试",
        "subject": "2",
        "price": 999,
        "applicablePerson": "2",
        "info": "11月15日软件测试"
    }

    response = requests.post(url,headers=headers,json=jsons)
    print(response.status_code)
    print(response.json())

if __name__ == '__main__':
    add_course()
