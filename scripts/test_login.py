from api.api_login import ApiLogin
from common.tools import assert_common



class TestLogin:
    #案例1：正常登录
    def test_login01(self):
        result = ApiLogin().api_login("admin", "HM_2023_test", "2")
        assert_common(result, 200, "操作成功",200)

    #案例2：登录失败（账号为空）
    def test_login02(self):
        result = ApiLogin().api_login("", "HM_2023_test", "2")
        assert_common(result, 200, "用户不存在/密码错误",500)

    #案例3：登录失败-用户名不存在
    def test_login03(self):
        result = ApiLogin().api_login("administ", "HM_2023_test", "2")
        assert_common(result, 200, "用户不存在/密码错误",500)

    #案例4：登录失败-密码错误
    def test_login04(self):
        result = ApiLogin().api_login("administ", "HM_2023_test1", "2")
        assert_common(result, 200, "用户不存在/密码错误",500)

    #案例5：登录失败-密码为空
    def test_login05(self):
        result = ApiLogin().api_login("administ", "", "2")
        assert_common(result, 200, "用户不存在/密码错误",500)

    #案例6：登录失败-code为空
    def test_login06(self):
        result = ApiLogin().api_login("administ", "HM_2023_test", "")
        assert_common(result, 200, "验证码错误",500)

    #案例7：登录失败-code错误
    def test_login07(self):
        result = ApiLogin().api_login("administ", "HM_2023_test", "3")
        assert_common(result, 200, "验证码错误",500)

    #案例8：登录失败-验证码类型不对
    def test_login08(self):
        result = ApiLogin().api_login("administ", "HM_2023_test", "张三")
        assert_common(result, 200, "验证码错误",500)

    #案例9：登录失败-密码类型不对
    def test_login09(self):
        result = ApiLogin().api_login("admin", "张三", "2")
        assert_common(result, 200, "用户不存在/密码错误",500)

    #案例10：登录失败-用户名类型不对
    def test_login10(self):
        result = ApiLogin().api_login("张三", "HM_2023_test", "2")
        assert_common(result, 200, "用户不存在/密码错误",500)


