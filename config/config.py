"""
    工程配置文件
"""
import os


#项目地址URL信息
BASE_URL = "http://kdtx-test.itheima.net"
BASE_User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"


#合同文件路径
#根目录
BASE_File_Path = os.path.dirname(os.path.abspath(__file__))
# config.py 在api_auto/config下，往上跳一层就是项目根
BASE_DIR = os.path.dirname(BASE_File_Path)