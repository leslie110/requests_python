# -*- coding:utf-8 -*-
import hashlib
import requests
def sha1_pwd(mima):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha1 = hashlib.sha1()
    sha1.update(mima.encode('utf-8'))
    encrypts = sha1.hexdigest()
    return encrypts
    print (encrypts)

url = "http://openapi.tlinx.cn/mct1/user/login"
data = {"user_name":"basic",
        "password":sha1_pwd("a123456"),
        "app":"iso"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}

re = requests.post(url,data=data,headers=headers)
print(re.json())