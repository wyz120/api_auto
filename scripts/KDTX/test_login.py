import pytest
from api.api_login import ApiLogin
from common.allure_log import api_log
from common.read_data import read_data
from common.tools import assert_common


data_list,case_ids = read_data("/data/login_test.json")
class TestLogin:
    """
        测试登录接口
    """
    @api_log
    @pytest.mark.aaa
    @pytest.mark.parametrize("case_id,case_name,username,password,verify_code,status_code,msg,code", data_list,ids=case_ids)
    def test_login(self, case_id, case_name, username, password, verify_code, status_code, msg, code):
        result = ApiLogin().api_login(username, password, verify_code)
        assert_common(result, status_code, msg,code)

