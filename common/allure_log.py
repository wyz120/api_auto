import allure
import json
from functools import wraps

def api_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 调用接口
        with allure.step(f"调用接口：{func.__name__}"):
            # 打印入参
            allure.attach(
                json.dumps(kwargs, ensure_ascii=False, indent=2),
                name="接口入参",
                attachment_type=allure.attachment_type.JSON
            )
            # 执行接口方法
            resp = func(*args, **kwargs)
            # 记录返回结果
            allure.attach(
                json.dumps(resp, ensure_ascii=False, indent=2),
                name="接口返回数据",
                attachment_type=allure.attachment_type.JSON
            )
        return resp
    return wrapper
