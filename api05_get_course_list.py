"""
    查询课程列表
"""
import requests
import config

url = config.BASE_URL+"/api/clues/course/list"
headers = config.BASE_HEADERS

respond = requests.get(url, headers=headers)
print(respond.json())