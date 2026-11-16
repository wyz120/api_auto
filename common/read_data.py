"""
读取测试数据模块
"""

import json
from config.config import BASE_DIR


#测试数据读取函数
def read_data():
    with open(f"{BASE_DIR}/data/login_test.json", "r", encoding="utf-8") as f:
        data_list = list()
        for i in json.load(f):
            data_list.append(tuple(i.values()))
        print(data_list)
        return data_list

if __name__ == "__main__":
    read_data()
