"""
pytest测试配置（fixture）
"""
import pytest
@pytest.fixture(scope='class')
def demo_func():
    print("\n 这是fixture前置操作 ")
    yield{"name": "张三", "age": 18}
    print("\n 这是fixture后置操作")

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成后，将收集到的item内的name和_nodeid中的中文转为utf-8
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
