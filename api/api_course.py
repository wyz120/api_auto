"""
    模块：课程管理
"""
import requests
import config
from utils import tools

class ApiCourse():
    #接口1：新增课程
    def add_course(self,name,subject,price,applicablePerson,info):
        url = config.BASE_URL+"/api/clues/course"
        headers = {
            "Authorization": tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent
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

    #接口2：查询课程列表
    def get_course_list(self,name):
        url = config.BASE_URL + "/api/clues/course/list?name=" + name
        headers = {
            "Authorization": tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent
        }

        respond = requests.get(url, headers=headers)
        return respond

    #接口3：查询课程
    def get_course(self,id):
        url = config.BASE_URL + "/api/clues/course/" + id
        headers = {
            "Authorization": tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent
        }

        respond = requests.get(url, headers=headers)
        return respond

    #接口4：修改课程
    def update_course(self,id,name,subject,price,applicablePerson,info):
        url = "https://kdtx-test.itheima.net/api/clues/course/"
        headers = {
            "Authorization": tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent,
            "Content-Type": "application/json"
        }
        jsons = {
            "id": id,
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson": applicablePerson,
            "info": info
        }

        respond = requests.put(url, headers=headers, json=jsons)
        print("请求body：", jsons)
        print("响应结果：", respond.text)
        return respond
    #接口5：删除课程
    def delete_course(self,id):
        url = config.BASE_URL + "/api/clues/course/" + id
        headers = {
            "Authorization": tools.get_token_func(),
            "User-Agent": config.BASE_User_Agent
        }

        respond = requests.delete(url, headers=headers)
        return respond
