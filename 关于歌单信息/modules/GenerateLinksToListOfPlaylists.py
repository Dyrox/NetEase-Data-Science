import requests
from lxml import etree


def link_gen():
    base = 'https://music.163.com'
    LINKS = []

    url = 'https://music.163.com/discover/playlist'

    headers = {
                'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
    response = requests.get(url=url,headers=headers)
    html = response.text
    html_elem = etree.HTML(html)

    playlist_hrefs = html_elem.xpath('//*[@id="cateListBox"]//*/*/*/a[@class="s-fc1 "]/@href')
    playlist_names = html_elem.xpath('//*[@id="cateListBox"]//*/*/*/a[@class="s-fc1 "]/text()')


    for href in playlist_hrefs:
        LINKS.append(base + href)

    #make a dictionary
    LINKS_DICT = dict(zip(playlist_names,LINKS))

    return LINKS_DICT

