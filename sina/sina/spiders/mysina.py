# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from sina import items
from scrapy.spiders import CrawlSpider,Rule#CrawlSpiders:定义了一些规则跟进link
from scrapy.linkextractors import LinkExtractor#提取链接

class MysinaSpider(CrawlSpider):
    name = 'mysina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_2.shtml','http://roll.news.sina.com.cn/news/gjxw/gdxw1/index_2.shtml']
    rules=[Rule(LinkExtractor(allow=('index_(\d+).shtml')),callback='getParse',follow=True)
           ]
    def getParse(self, response): #重命名逻辑方法
        newsList = response.xpath("//ul[@class='list_009']/li")
        for news in newsList:

            item = items.SinaItem() #对其进行实例化
            newsTitle = news.xpath('./a/text()')[0].extract()
            newsUrl = news.xpath('./a/@href')[0].extract()
            newsTime = news.xpath('./span/text()')[0].extract()
            content = self.getContent(newsUrl)

            item['newsTitle'] = newsTitle
            item['newsUrl'] = newsUrl
            item['newsTime'] = newsTime
            item['content'] = content
            yield item

    def getContent(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }
        response = requests.get(url,headers=headers).content.decode('utf-8','ignore')   #content二进制
        mytree = etree.HTML(response)
        contentList = mytree.xpath("//div[@class='article']//text()")
        print(contentList)
        content = ''
        for c in contentList:
            #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            content += c.strip().replace('\n','')  #保证content为整片文章
        return content
#方法二
# -*- coding: utf-8 -*-
'''import scrapy
import requests
from lxml import etree
from sina import items

from scrapy.spiders import CrawlSpider,Rule  #CrawlSpiders:定义了一些规则跟进link
from scrapy.linkextractors import LinkExtractor  #提取链接

class MysinaSpider(CrawlSpider):
    name = 'mysina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_2.shtml']
    rules = [Rule(LinkExtractor(allow=('index_(\d+).shtml')),callback='getParse',follow=True)]

    def getParse(self, response):

        newsList = response.xpath("//ul[@class='list_009']/li")
        for news in newsList:

            newsTitle = news.xpath('./a/text()')[0].extract()
            newsUrl = news.xpath('./a/@href')[0].extract()
            newsTime = news.xpath('./span/text()')[0].extract()

            #构造请求(修改为框架Request构造请求)
            request = scrapy.Request(newsUrl,callback=self.getMataContent) #回调为getMataContent
            #使用meta传参
            request.meta['newsTitle'] = newsTitle
            request.meta['newsUrl'] = newsUrl
            request.meta['newsTime'] = newsTime
            yield request

    def getMataContent(self,response):

        #getMataContent接受来自request请求后的响应response

        contentList = response.xpath("//div[@class='article']//text()")
        content = ''
        for c in contentList:
            content += c.extract().strip()
        item = items.SinaItem()
        #response响应数据对应字段赋值给item
        item['newsTitle'] = response.meta['newsTitle']
        item['newsUrl'] = response.meta['newsUrl']
        item['newsTime'] = response.meta['newsTime']
        item['content'] = content
        yield item
'''