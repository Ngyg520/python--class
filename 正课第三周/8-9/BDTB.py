"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第三周
@author:Mr.Yang
@file:使用类和对象封装百度贴吧爬虫.PY
@ide:PyCharm
@time:2018-08-09 09:18:32
"""
import urllib.request
import re
import random
from urllib.request import ProxyHandler,build_opener

class BDTBSpider(object):
    user_agent_list = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    ip_list = [{'http': 'http://61.135.217.7:80'}, {'http': 'http://121.31.148.15:8123'},{'http': 'http://1.194.122.221:8010'}]
    def __init__(self,tieba_id):
        #贴吧ID是创建对象的时候,传递过来的值,然后赋值给了self.tieba_id这个属性,
        self.tieba_id=tieba_id
        #然后再将tirba_id这个值和原网址进行拼接得到帖子的完整链接
        self.base_url="https://tieba.baidu.com/p/{}".format(self.tieba_id)
        #设置请求头,从请求头列表随机选择一个浏览器标识设置请求头
        self.headers={'user-Agent':random.choice(self.user_agent_list)}
        #设置ip,从ip_list这个列表中当中随机选择一个代理IP,根据这个ip创建代理对象
        self.ip=random.choice(self.ip_list)

    #定义一个获取总页数的函数,目的是为了能自动爬取所有页数的数据
    def get_total_page(self):
        #创建request对象
        request=urllib.request.Request(url=self.base_url,headers=self.headers)
        #创建IP代理对象
        ip_proxyhandler=ProxyHandler(self.ip)
        #创建opener对象
        opener=build_opener(ip_proxyhandler)
        #根据opener对象调用opener方法对网页发起请求.拿到源代码
        reponse=opener.open(request).read().decode('utf-8')
        #创建正则表达式规则
        patter_obj=re.compile(r'<span class="red">(.*?)</span>',re.S)
        #通过调用re.search这个函数从源代码中获取总页数
        #由于拿到的total_page是字符串,所以要使用int转换成整数
        total_page=int(re.search(patter_obj,reponse)[1])
        #再get_total_page这个函数中,调用get_user_and_comment这个函数,并且把total_page当做实参传递给get_user_and_comment这个函数的形参,这个时候,total_page这个形参就接受到了total_page这个实参
        self.get_user_and_comment(total_page)

    #定义一个获取详细信息的函数
    #定义一个形参,接受get_total_page函数中的total_page,目的是为了在get_user_and_comment函数中接收total_page来使用
    def get_user_and_comment(self,total_page_1):
        #遍历所有页,拿到每一页的页码,page_num指的就是每一页的页码
        for page_num in range(1,total_page_1+1):
            print('正在爬取第{}页'.format(page_num))
            #拼接完整的url
            abs_url=self.base_url+"?pn="+str(page_num)

            request=urllib.request.Request(url=abs_url,headers=self.headers)
            ip_pro_handler=ProxyHandler(self.ip)
            opener=build_opener(ip_pro_handler)
            response=opener.open(request).read().decode('utf-8')

            #定义正则表达式规则,从每一页中提取想要的数据信息
            pattern_obj=re.compile(r'<a.*?class="p_author_name.*?>(.*?)</a>.*?<div id="post_content.*?>(.*?)</div>',re.S)
            #使用findall匹配每一页中的所需要的数据,返回值是一个列表,里面套着元组,一个元组对应着一个用户的昵称还有用户信息
            result_list=re.findall(pattern_obj,response)
            #将匹配到的result_list的数据,放置到update_date这个函数中进行处理
            self.update_data(result_list)
    #定义一个函数来处理匹配到的数据
    def update_data(self,result_list):
        remove_n = re.compile(r'\n', re.S)
        remove_br = re.compile(r'<br>', re.S)
        remove_img = re.compile(r'(.*?)<img', re.S)
        remove_space=re.compile(r' ',re.S)
        #遍历result_list,,每一个tuple_data对应着一个元组的信息,每一个元组存放着用户昵称和用户回复信息
        for tuple_data in result_list:
            #先判断用户昵称中是否含有img,如果有进行相应的清理数据的工作
            if "img" in tuple_data[0]:
                #存在img这个字符串,通过search将昵称匹配出来,去除掉后面跟着的img
                nick_name=re.search(remove_img,tuple_data[0])[1]
            else:
                #如果名字中不包含img这个字符串,则说明是一个正常的昵称,不需要做正常的处理
                nick_name=tuple_data[0]
            nick_name = re.sub(remove_space,'',nick_name)
            #先判断用户回复中是否含有img,如果有进行相应的数据清理工作
            if "img"in tuple_data[1]:
                content=re.search(remove_img,tuple_data[1])[1]
            else:
                content=tuple_data[1]
            #将content里面的\n,<br/>这个换行符取出掉,替换成空
            new_content=re.sub(remove_n,'',content)
            new_content_1=re.sub(remove_br,'',new_content)
            new_space=re.sub(remove_space,'',new_content_1)
            #将nick_name和new_content放置到元组中进行返回
            new_tuple=(nick_name,new_space)

            self.save_data(new_tuple)
    #定义一个函数来存储数据
    def save_data(self,new_tuple):
        #接受new_tuple进行数据的存储
        # 使用self.tieba_id来进行命名
        #由于save_data是在update_data这个函数的for循环中调用的,所以一旦使用 W模式打开文件,就会不断覆盖前一页的内容,所以使用a+追加写入
        file_test=open("{}.txt".format(self.tieba_id),'a+',encoding='utf-8')
        file_test.write('用户昵称:{}'.format(new_tuple[0]))
        file_test.write("\n")
        file_test.write("用户回复:{}".format(new_tuple[1]))
        file_test.write("\n")
        file_test.write("--------------------")
        file_test.write("\n")

    #设置一个爬虫的启动函数
    def start_spider(self):
        print('百度贴吧爬虫以启动!')
        self.get_total_page()

if __name__ == '__main__':
    Spider=BDTBSpider('5831574532')
    Spider.start_spider()




