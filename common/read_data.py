"""
读取测试数据模块
"""

import json
from config.config import BASE_DIR


#测试数据读取函数
def read_data(path):
    with open(f"{BASE_DIR}{path}", "r", encoding="utf-8") as f:
        data = json.load(f)
        #存放用例参数
        data_list = []
        #存放用例id和名称
        ids_list = []

        for item in data:
            data_list.append((item['case_id'], item['case_name'],item['username'], item['password'], item['verify_code'], item['status_code'], item['msg'], item['api_code']))
            ids_list.append(f"{item['case_id']}-{item['case_name']}")

        return data_list, ids_list

if __name__ == "__main__":
    read_data()
