__author__ = 'Administrator'
from scrapy.spider import CrawlSpider,Rule,Request
from scrapy.linkextractors import LinkExtractor
from scrapy import FormRequest# scrapy 中用作登陆使用的一个包
from qichezhijia.items import QichezhijiaItem
class qichezhijiaSpider(CrawlSpider):
    name='qichezhijia'
    allowed_domains=['autohome.com.cn']
    start_urls=['https://www.autohome.com.cn/shanghai/']
    rules=(Rule(LinkExtractor(allow='\.html$'),callback='parse_item',follow=True),)

    def parse_item(self,response):
        print(response.url)
        qichezhijia=QichezhijiaItem()
        qichezhijia['url']=response.url
        yield qichezhijia

