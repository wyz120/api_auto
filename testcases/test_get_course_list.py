from api.api_course import ApiCourse


class TestGetCourseList():
    #案例1：正常查询
    def test_get_course_list01(self):
        result = ApiCourse().get_course_list("11月15日软件测试")
        print(result.json())
        assert result.status_code == 200
        assert result.json()["code"] == 200
        assert result.json()["rows"][0]["name"] == "11月15日软件测试"
