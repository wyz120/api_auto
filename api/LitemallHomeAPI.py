import requests
from config.config import mall_url

def MallHome():
    """
    获取session
    :return:
    """
    url = f"{mall_url}/index.php?m=Home&c=User&a=verify"
    response = requests.get(url)
    cookies = response.cookies
    session = cookies.get("PHPSESSID")
    return session
