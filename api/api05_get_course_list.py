"""
    查询课程列表
"""
import requests
import config
from utils import tools
def get_course_list(name):

    url = config.BASE_URL+"/api/clues/course/list?name="+name
    headers = {
        "Authorization": tools.get_token_func(),
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    }

    respond = requests.get(url, headers=headers)
    return respond
