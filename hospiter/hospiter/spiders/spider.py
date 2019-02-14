__author__ = 'Administrator'
import scrapy
from hospiter.items import HospiterItem
class hospitalSpider(scrapy.Spider):
    name='hospital'
    allowed_domains=['yixuezp.com']
    start_urls=['http://www.yixuezp.com/zhaopin?page={}'.format(i) for i in range(1,700)]
    def parse(self, response):
        #print(response.text)
        node_list=response.xpath('//div[@class="newsjob"]/ul/li')

        items=[]
        for node in node_list:
            item=HospiterItem()
            hospitalName=node.xpath('./p[1]/a/text()').extract()[0]
            hospitalSize=node.xpath('./span[1]/text()').extract()
            hospitalAddress=node.xpath('./span[2]/text()').extract()
            hospitalDesc=node.xpath('./p[2]/a/text()').extract()
            item['hospitalName']=hospitalName
            item['hospitalSize']=hospitalSize
            item['hospitalAddress']=hospitalAddress
            item['hospitalDesc']=hospitalDesc
            items.append(item)
            return items # 如果直接return的话，一页数据只会返回一条数据
            #yield item #用yield 的话，可以交给下载器，继续执行下一步操作。

