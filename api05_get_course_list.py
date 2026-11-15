"""
    查询课程列表
"""
import requests
import config
import tools

url = config.BASE_URL+"/api/clues/course/list"
headers = {
    "Authorization":tools.get_token_func(),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
}

respond = requests.get(url, headers=headers)
print(respond.json())