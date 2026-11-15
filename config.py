"""
    工程配置文件
"""
import tools

#项目地址URL信息
BASE_URL = "http://kdtx-test.itheima.net"

#请求的headers
BASE_HEADERS = {
    "Authorization":tools.get_token_func(),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
}