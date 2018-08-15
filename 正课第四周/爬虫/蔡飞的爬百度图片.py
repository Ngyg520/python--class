"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第四周
@author:Mr.Yang
@file:瑞文额吧.PY
@ide:PyCharm
@time:2018-08-13 22:52:38
"""
from urllib.parse import urlencode
import requests, time, random, json, os


class BDTPSpider(object):
    User_Agent_List = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    ]

    ip_list = []

    n = 0

    keyword = input('请输入你要爬取的图片名:')

    local_path = 'C:/Users/Administrator/Desktop/bd/'

    def __init__(self):
        self.base_url = 'https://image.baidu.com/search/acjson?'
        self.headers = {'User-Agent': random.choice(self.User_Agent_List), "referer": "https://image.baidu.com"}
        self.ip = random.choice(self.ip_list)

    def get_page(self, offset):
        params = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': self.keyword,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '0',
            'word': self.keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'pn': offset,
            'rn': '30',
            'gsm': '5a',
            str(time.time())[0:14].replace('.', ''): ''
        }
        url = self.base_url + urlencode(params)
        print('当前网址为"%s"' % url)
        print('当前随机ip为%s' % self.ip)
        try:
            response = requests.get(url, headers=self.headers, proxies=self.ip)
            if response.status_code == 200:
                html = response.text
                self.parse_json(html)
        except Exception as e:
            print('失败原因是:', e)

    def parse_json(self, html):
        json_data = json.loads(html)
        if json_data.get("data"):
            for item in json_data.get("data"):
                img_list_url = item.get('thumbURL')
                time.sleep(1)
                if img_list_url:
                    self.save_img(img_list_url)
                else:
                    continue

    def save_img(self, img_list_url):
        if not os.path.exists(self.local_path):
            os.mkdir(self.local_path)
        try:
            response = requests.get(img_list_url, headers=self.headers, proxies=self.ip)
            if response.status_code == 200:
                with open(self.local_path + '%s.jpg' % self.n, 'wb')as f:
                    f.write(response.content)
                    print('Bingo!下载成功，当前是%d张图' % self.n)
                    time.sleep(1)
                    self.n += 1
        except Exception as e:
            print('保存图片失败，原因是：', e)

    def start_spider(self):
        page = int(input('请输入你要爬取的页数：'))
        for i in range(0, page * 30 + 30, 30):
            self.get_page(i)


if __name__ == '__main__':
    se = BDTPSpider()
    se.start_spider()
