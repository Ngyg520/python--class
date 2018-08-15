"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:使用类和对象封装糗事百科爬虫.PY
@ide:PyCharm
@time:2018-08-08 14:17:45
"""
import random
import urllib.request
import re
import sqlite3
from urllib.request import ProxyHandler,build_opener

class DataTool(object):
    remove_n=re.compile(r'\n')
    remove_br = re.compile(r'<br/>')
    remove_quot = re.compile(r'&quot:')
    #定义一个函数用来去除爬虫类中返回出来的元组里面的\n,<br/>,&quot等不需要的数据
    @classmethod
    def update_tuple(cls,tuple_data):
        #将tuple_data这个元组的第0个元素(用户昵称)中的\n给去除掉
        nick_name=re.sub(cls.remove_n,'',tuple_data[0])
        age=tuple_data[1]
        content=re.sub(cls.remove_n,'',tuple_data[2])
        content=re.sub(cls.remove_br,'', content)
        content=re.sub(cls.remove_quot,'',content)
        smile_num=tuple_data[3]
        comment_num=tuple_data[4]
        new_tuple=(nick_name,age,content,smile_num,comment_num)
        return new_tuple

class DBManager(object):
    connect=None
    cursor=None
    @classmethod
    def create_connect_and_cursor(cls):
        cls.connect=sqlite3.connect('qsbk_pius.db')
        cls.cursor=cls.connect.cursor()
    @classmethod
    def create_table(cls):
        create_table_sql="create table if not EXISTS baike(id INTEGER PRIMARY KEY ,nick_name VARCHAR ,age VARCHAR ,content VARCHAR ,smile_num VARCHAR ,comment_num VARCHAR )"
        cls.cursor.execute(create_table_sql)
    @classmethod
    def insert_data(cls,new_tuple):
        insert_sql="insert into baike(nick_name,age,content,smile_num,comment_num)VALUES('%s','%s','%s','%s','%s')"%(new_tuple[0],new_tuple[1],new_tuple[2],new_tuple[3],new_tuple[4])
        cls.cursor.execute(insert_sql)
    @classmethod
    def close_connect_and_cursor(cls):
        cls.connect.commit()
        cls.cursor.close()
        cls.connect.close()

class QSBKpoder(object):
    user_agent_list = ['Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11']
    ip_list = [{'http': 'http://111.155.116.200:8123'}, {'http': 'http://139.129.166.68:3128'},{'http': 'http://118.190.95.35:9001'}]
    def __init__(self):
        self.base_url="https://www.qiushibaike.com/hot/"#网址
        self.headers={'User-Agent':random.choice(self.user_agent_list)}#标识头
        self.ip=random.choice(self.ip_list)#代理IP
    #定义一个获取网页源代码的函数
    def get_origin_page_code(self,page_num):
        #page_num标签当前页的页码
        print('正在爬取第{}页数据'.format(page_num))
        #拼接网址
        ads_url=self.base_url+"page/"+str(page_num)+"/"
        #创建request对象
        request=urllib.request.Request(ads_url,headers=self.headers)
        #创建ip代理对象
        proxy_handler=ProxyHandler(self.ip)
        #创建opener对象
        opener=build_opener(proxy_handler)
        try:
            response=opener.open(request)
        except Exception as e:
            print('链接失败的原因',e)
        else:
            html_string=response.read().decode('utf-8')
            return html_string
    #定义一个网页提取数据的函数
    def get_info_by_page_code(self,html_string):
        pattern_obj=re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender .*?Icon">(.*?)</div>.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
        result_list=re.findall(pattern_obj,html_string)
        #遍历正则匹配出来的数据的列表遍历出来的每一个tuple_data都是一个元组
        for tuple_data in result_list:
            #tuple_data('用户''age'')
            new_tuple=DataTool.update_tuple(tuple_data)
            DBManager.insert_data(new_tuple)

if __name__=='__main__':
    DBManager.create_connect_and_cursor()
    DBManager.create_table()
    spider=QSBKpoder()
    for x in range(1,11):
        html_string=spider.get_origin_page_code(x)
        spider.get_info_by_page_code(html_string)
    DBManager.close_connect_and_cursor()
