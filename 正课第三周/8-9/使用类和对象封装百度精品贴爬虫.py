"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:使用类和对象封装百度精品贴爬虫.PY
@ide:PyCharm
@time:2018-08-09 15:55:16
"""
import urllib.request
from urllib.request import ProxyHandler,build_opener
from BDTB import BDTBSpider
class JPTSpider(BDTBSpider):
    #tie_ba_name是贴吧的名字,是创建JPTSpider类生成的对象的时候,会给这个形参传值
    def __init__(self,tie_ba_name):
        super(JPTSpider, self).__init__(tieba_id="")
        self.url=""
    #定义一个函数用来获取所有精品帖子的个数
    def get_total_tie_zi_num(self):
        #self.headers是从父类继承过来的
        request=urllib.request.Request(url=self.url,headers=self.headers)
        ip_proxyhandler=ProxyHandler(self.ip)
        opener=build_opener(ip_proxyhandler)
