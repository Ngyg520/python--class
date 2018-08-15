"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:使用requests和cookie模拟登陆github.PY
@ide:PyCharm
@time:2018-08-15 14:23:29
"""
# 首先要做模拟登录需要知道表单数据的提交地址和提交的参数,经观察发现点击登录发起的是一个post请求,请求的地址是:https://github.com/session,提交的参数的参数中commit,utf-8这个参数是不会变化的,login这个参数是自己填写的账户名,password这份参数是自己添加的密码,身下的这个authenticity_token这个参数是一个加密参数,经过分析authenticity_token这个参数是在登录页面源代码里面可以找到,,也就是说,只要访问登录页面,拿到源代码就可以获取authenticity_token这个参数,到目前为止,五个参数的值都可以拿到,下面就可以进行模拟登陆
import requests
import re
class Login_GitHub(object):
    def __init__(self):
        self.headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Host":"github.com",
            "Referer":"https://github.com/login"
        }
        self.login_url="https://github.com/login"
        self.post_url="https://github.com/session"
        self.session=requests.Session()
        self.logined_url="https://github.comsettings/profile"
    #定义一个函数来获取authenticity_token这个参数的值
    def get_authenticity_token(self):
        response=self.session.get(self.login_url,headers=self.headers).text
        pattern_obj=re.compile(r'authenticity_token.*?value="(.*?)" />',re.S)
        authenticity_token=re.search(pattern_obj,response)[1]
        # print(authenticity_token)
        return authenticity_token

#拿到authenticity_token这个参数就可以进行模拟登录了,
    def login(self,login,password):
        post_data={
            "commit":"Sign+in",
            "utf8":"√",
            "authenticity_token":self.get_authenticity_token(),
            "login":login,
            "password":password
        }
        response=self.session.post(self.post_url,data=post_data,headers=self.headers)
        if response.status_code==200:
            print('登录成功!')
            response=self.session.get(self.logined_url,headers=self.headers)
            print(response.text)

if __name__ == '__main__':
    github=Login_GitHub()
    # github.get_authenticity_token()
    github.login("Ngyg520","yyj199707111")

