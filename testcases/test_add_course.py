import unittest

from api.api_course import ApiCourse
import json

class TestAddCourse():
    #案例1：新增成功
    def test_add_course01(self):
        result = ApiCourse().add_course("11月15日软件测试", "2", "999", "2", "11月15日软件测试")
        print(result.json())
        assert result.status_code == 200
        assert result.json()["code"] == 200
        assert result.json()["msg"] == "操作成功"