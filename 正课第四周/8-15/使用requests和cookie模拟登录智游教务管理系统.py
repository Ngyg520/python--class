"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:使用requests和cookie模拟登录智游教务管理系统.PY
@ide:PyCharm
@time:2018-08-15 11:32:55
"""
import requests
class LoginZhiyou(object):
    def __init__(self):
        self.post_url="http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        self.session=requests.Session()
    def login(self,username,password):
        data={
            'j_username':username,
            'j_password':password
        }
        response=requests.post(self.post_url,data=data,headers=self.headers)
        print(response.text)
    def is_login(self):
        resopnse=requests.get("http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr",headers=self.headers)
        if resopnse.status_code==200:
            print('登录状态:',resopnse.text)
        else:
            print('非登录状态')
if __name__ == '__main__':
    zhiyou=LoginZhiyou()
    zhiyou.login("18738577851","yyj19970711")
    zhiyou.is_login()