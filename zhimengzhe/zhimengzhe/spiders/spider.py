__author__ = 'Administrator'
import scrapy
from zhimengzhe.items import ZhimengzheItem
class zhiSpider(scrapy.Spider):
    name = 'zhimengzhe'
    allowed_domains=['zhimengzhe.com']
    start_urls=['http://www.zhimengzhe.com/bianchengjiaocheng/qitabiancheng/index_{}.html'.format(n) for n in range(2,1000)]
    def parse(self, response):
        print(response.text)
        nodes_list=response.xpath("//ul[@class='list-unstyled list-article']/li")
        items=[]
        for node in nodes_list:
            zhiTitle=node.xpath('./h3/a/text()').extract()
            zhiUrl=node.xpath('./h3/a/@href').extract()
            zhiTime=node.xpath('./div/span[@class="data"]/text()').extract()
            item=ZhimengzheItem()
            item['zhiTitle']=zhiTitle
            item['zhiUrl']=zhiUrl
            item['zhiTime']=zhiTime
            items.append(item)
            yield item
