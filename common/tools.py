"""
    工具封装
"""
import requests
from api.api_login import ApiLogin
import config

#登录token获取封装
def get_token_func():
    result = ApiLogin().api_login("admin", "HM_2023_test", "2")
    token = result.json().get("token")
    try:
        return token
    except Exception as e:
        print(e)

#断言函数封装
def assert_common(result,status_code,msg,code):
    """断言函数封装
    :param result:响应结果
    :param status_code:状态码
    :param msg:响应消息
    :param code:响应码
    """
    assert result.status_code == status_code
    try:
        assert result.json().get("msg") == msg
        assert result.json().get("code") == code
    except:
        assert result.text == msg
