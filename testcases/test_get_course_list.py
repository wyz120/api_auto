from api.api_course import ApiCourse
from common.tools import assert_common


class TestGetCourseList():
    #案例1：正常查询
    def test_get_course_list01(self):
        result = ApiCourse().get_course_list("11月15日软件测试")
        print(result.json())
        assert_common(result, 200, "查询成功", 200)
