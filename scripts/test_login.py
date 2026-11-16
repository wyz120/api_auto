import pytest

from api.api_login import ApiLogin
from common.read_data import read_data
from common.tools import assert_common

data_list = read_data()
case_ids = [f"案例{i + 1}" for i in range(len(data_list))]
class TestLogin:
    """
        测试登录接口
    """
    @pytest.mark.parametrize("username,password,image_code,status_code,msg,code", data_list,ids=case_ids)
    def test_login(self,username,password,image_code,status_code,msg,code):
        result = ApiLogin().api_login(username, password, image_code)
        assert_common(result, status_code, msg,code)

