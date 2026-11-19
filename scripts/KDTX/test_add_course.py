import unittest

import pytest

from api.api_course import ApiCourse
from common.allure_log import api_log
from common.tools import assert_common

class TestAddCourse():
    @api_log
    @pytest.mark.aaa
    #案例1：新增成功
    def test_add_course01(self):
        result = ApiCourse().add_course("11月15日软件测试", "2", "999", "2", "11月15日软件测试")
        assert_common(result, 200, "操作成功", 200)
