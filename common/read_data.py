"""
读取测试数据模块
"""

import json
from config.config import BASE_DIR


#测试数据读取函数
def read_data():
    with open(f"{BASE_DIR}/data/login_test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

if __name__ == "__main__":
    read_data()
