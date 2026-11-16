"""
    工具封装
"""
import requests
from api.api_login import ApiLogin
import config


def get_token_func():
    result = ApiLogin().api_login("admin", "HM_2023_test", "2")
    token = result.json().get("token")
    try:
        return token
    except Exception as e:
        print(e)
