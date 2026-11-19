"""
测试模块：合同管理
"""
from api.api_contract import ApiContract
from common.allure_log import api_log
from common.tools import assert_common
import pytest

class TestAddContract:
    id = ""
    #案例1：上传合同
    @pytest.mark.aaa
    @api_log
    def test_upload_contract(self):
        result = ApiContract().upload_file_name()
        assert_common(result, 200, "操作成功", 200)
    #案例2：新增合同
    @api_log
    @pytest.mark.bbb
    def test_add_contract(self):
        result = ApiContract().add_contract("测试合同","18238199876","2")
        assert_common(result,200,"操作成功",200)
    @api_log
    #案例3：查询合同列表
    @api_log
    @pytest.mark.aaa
    def test_query_contract_list(self):
        result = ApiContract().query_contract_list("18238199876")
        TestAddContract.id = result.json()["rows"][0]["id"]
        assert_common(result, 200, "查询成功", 200)
    @api_log
    @pytest.mark.bbb
    #案例4：删除合同
    def test_delete_contract(self):
        result = ApiContract().delete_contract(TestAddContract.id)
        assert_common(result, 200, "删除成功！", 200)

