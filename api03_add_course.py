"""
新增课程
"""
import requests
from api02_login import login

def add_course():
    token = login()
    url = "http://kdtx-test.itheima.net/api/clues/course"
    headers = {
        "content-type": "application/json",
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }
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
