"""
pytest测试配置（fixture）
"""
import pytest
from common.db_util import DBUtil
from config.config import BASE_PATH
import yaml
@pytest.fixture(scope='class')
def demo_func():
    print("\n 这是fixture前置操作 ")
    yield{"name": "张三", "age": 18}
    print("\n 这是fixture后置操作")


@pytest.fixture(scope="session")
def db():
    with open(f"{BASE_PATH}/config.yaml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    db = DBUtil(**cfg["db"])
    yield db
    db.close()
