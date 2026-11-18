import pytest

from api.api_login import ApiLogin
from common.allure_log import api_log
from common.read_data import read_data
from common.tools import assert_common


raw_data = read_data()
#空集合，存放用例文件内读取的数据
data_list = []
#空集合，存放用例的id和名称
case_ids = []
# 遍历读取的用例数据，将数据添加到data_list和case_ids中
for item in raw_data:
    data_list.append((item['case_id'], item['case_name'], item['username'], item['password'], item['image_code'], item['status_code'], item['msg'], item['code']))
    case_ids.append(f"{item['case_id']}-{item['case_name']}")


class TestLogin:
    """
        测试登录接口
    """
    @api_log
    @pytest.mark.aaa
    @pytest.mark.parametrize("case_id,case_name,username,password,image_code,status_code,msg,code", data_list,ids=case_ids)
    def test_login(self, case_id, case_name, username, password, image_code, status_code, msg, code):
        result = ApiLogin().api_login(username, password, image_code)
        assert_common(result, status_code, msg,code)

