import pytest
from api.LitemallLoginAPI import MALL_LOGIN
from common.read_data import read_data

data_list,ids_list = read_data("/data/mall_login_test.json")

@pytest.mark.aaa
@pytest.mark.parametrize("case_id,case_name,username,password,verify_code,status_code,msg,api_code", data_list,ids=ids_list)
def test_mall_login(case_id, case_name, username, password, verify_code, status_code, msg, api_code):
    respond = MALL_LOGIN(username, password, verify_code)
    assert respond.status_code == status_code
    assert respond.json().get("msg") == msg
    assert respond.json().get("status") == api_code
