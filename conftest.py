"""
pytest使用
"""
import pytest
@pytest.fixture(scope='class')
def demo_func():
    print("\n 这是fixture前置操作 ")
    yield{"name": "张三", "age": 18}
    print("\n 这是fixture后置操作")
