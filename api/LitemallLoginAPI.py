import requests
from api.LitemallHomeAPI import MallHome
from config.config import mall_url


def MALL_LOGIN(username, password, verify_code):
    url = f"{mall_url}/index.php?m=Home&c=User&a=do_login"
    cookie = {
        "PHPSESSID": MallHome()
    }
    json = {
        "username": username,
        "password": password,
        "verify_code": verify_code
    }
    respond = requests.post(url,cookies=cookie,data=json)
    return respond

