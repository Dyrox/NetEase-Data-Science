import requests
from lxml import etree
import json
import time
import random
import os
from PlaylistLinkGen import link_gen

folder_path = 'playlistdata'

class Netease_spider:
    # 初始化数据
    def __init__(self,url = 'https://music.163.com/discover/playlist'):
        url = url.replace('#','')
        self.originURL = url
        self.data = []

    # 获取网页源代码
    def get_page(self,url):
        headers = {
            'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers)
        html = response.text
        return html

    # 解析网页源代码，获取数据
    def parse4data(self,html):
        html_elem = etree.HTML(html)
        span_element = html_elem.xpath('//*[@id="m-disc-pl-c"]/div/div[1]/h3/span')[0]
        self.style = span_element.text
        play_num = html_elem.xpath('//ul[@id="m-pl-container"]/li/div/div/span[@class="nb"]/text()')
        song_title = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[1]/a/@title')
        song_href = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[1]/a/@href')
        song_link = ['https://music.163.com/#'+item for item in song_href]
        user_title = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[2]/a/@title')
        user_href = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[2]/a/@href')
        user_link = ['https://music.163.com/#'+item for item in user_href]
        data = list(map(lambda a,b,c,d,e:{'歌单名称':a,'播放量':b,'歌单链接':c,'用户名称':d,'用户链接':e},song_title,play_num,song_link,user_title,user_link))
        return data

    # 解析网页源代码，获取下一页链接
    def parse4link(self,html):
        html_elem = etree.HTML(html)
        href = html_elem.xpath('//div[@id="m-pl-pager"]/div[@class="u-page"]/a[@class="zbtn znxt"]/@href')
        if not href:
            return None
        else:
            return 'https://music.163.com/' + href[0]
        
    def write_to_file(self,data):
        filename = f'{key}歌单数据.json'
        filename = filename.replace('/',' ')
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def sort_by_plays(self,data):
        data_after_sort = sorted(data,key=lambda item:int(item['播放量'].replace('万','0000')),reverse=True)
        return data_after_sort

    # 开始爬取网页
    def crawl(self):
        # 爬取数据
        print('爬取数据')
        html = self.get_page(self.originURL)
        data = self.parse4data(html)
        self.data.extend(data)
        link = self.parse4link(html)
        while(link):
            html = self.get_page(link)
            data = self.parse4data(html)
            self.data.extend(data)
            link = self.parse4link(html)
            time.sleep(random.random())
        # 处理数据，按播放 量进行排序
        print('处理数据')
        data_after_sort = self.sort_by_plays(self.data)
        # 写入文件
        print('写入文件')
        self.write_to_file(data_after_sort)
        print('写入完成')


LINKS_DICT = link_gen()

if not os.path.exists(folder_path):
        os.mkdir(folder_path)

for key,value in LINKS_DICT.items():
    print(f'\033[92m正在处理{key}歌单\033[0m')

    filename = f'{key}歌单数据.json'
    filename = filename.replace('/',' ')
    file_path = os.path.join(folder_path, filename)

    
    if os.path.exists(file_path):
        print(f'\033[91m{key}歌单数据已存在，跳过\033[0m')
        continue
    spider = Netease_spider(value)
    spider.crawl()


print(f'\033[93m处理完成\033[0m')
