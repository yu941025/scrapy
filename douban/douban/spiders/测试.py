__author__ = 'Administrator'
import requests
from lxml import etree
url='https://music.douban.com/subject/1406522/'

resp=requests.get(url=url)
#print(resp.text)
html=etree.HTML(resp.text)
h=html.xpath('//*[@property="v:summary"]/text()')
a=html.xpath('//*[@id="link-report"]/div[@property="v:description"]/text()')
print(a)