"""
    上传合同文件
"""
import requests

import config
import tools

url = config.BASE_URL+"/api/common/upload"
headers = {
    "Authorization": tools.get_token_func(),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36",
    # "Content-Type": "multipart/formdata"
    #注意：使用files 参数时，request 库会自动添加"Content-Type": "multipart/formdata"类型，不必再手动添加，否则会报错！
}
files = {
    "file": open("./demo.pdf","rb")#说明：rb以二进制的方式读取
}
respond = requests.post(url,headers=headers,files=files)
print(respond.status_code)
print(respond.json())