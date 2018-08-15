"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:曹森真的傻.PY
@ide:PyCharm
@time:2018-08-13 20:17:31
"""
import urllib.request
import json
import os
from urllib.parse import urlencode
from urllib.request import ProxyHandler,build_opener#拼接网址
import random
import time
import requests
#头.ip
photo_name_dict={}
class BDPhoto (object):
    user_agent_list = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    ip_list = [{'http': 'http://61.135.217.7:80'}, {'http': 'http://121.31.148.15:8123'},{'http': 'http://1.194.122.221:8010'}]

    def __init__(self):
        self.base_url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=美女背景图&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=美女背景图&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&"
        #设置请求头,从请求头列表随机选择一个浏览器标识设置请求头
        self.headers={'user-Agent':random.choice(self.user_agent_list)}
        #设置ip,从ip_list这个列表中当中随机选择一个代理IP,根据这个ip创建代理对象
        self.ip=random.choice(self.ip_list)
#pn=30&rn=30&gsm=1fe&1534163775556=

    def get_page(self,gsm):
        for num in (30,30):
            params={
                "pn":num,
                "rn":"30",
                "gsm":gsm,
                str(time.time())[0:14].replace('.', ''):"",
            }

            url_1=self.base_url+urlencode(params)
            # print(url_1)
            try:
                response = requests.get(url_1, headers=self.headers, proxies=self.ip)
                if response.status_code == 200:
                    html = response.text
                    self.parse_json(html)
            except Exception as e:
                print('失败原因是:', e)

        #定义一个函数来解析json数据
    def parse_json(self, html):
        # 由于网页源代码是字符串,所以需要调用loads方法进行反序列化,得到一个字典对象
        json_data = json.loads(html)
        gsm = json_data.get('gsm')

        # 先判断json_data这个字典当中有没有data这个键
        if json_data.get('data'):
            # 如果有data这个键,则将这个键对应的列表取出来,并遍历json_data对应的列表,每一个item对应的都是一个字典
            for item in json_data.get('data'):
                # 将item这个字典里面的键"thumbURL"取出来,对应的结果是一个
                thumbURL= item.get("thumbURL")
                di= item.get('di')
                photo_name_dict[di]=thumbURL
                self.dowloads_Photo(photo_name_dict)
                self.again_data(gsm)
    def dowloads_Photo(self,photo_name_dict):
        for di,thumbURL in photo_name_dict.items():
            urllib.request.urlretrieve(thumbURL,'./image/{}.jpg'.format(di))
            print('正在下载%s'%di)

    def again_data(self,gsm,):
        print(gsm)
        self.get_page(gsm)
duixiang=BDPhoto()
duixiang.get_page("b4")
