__author__ = 'Administrator'
import scrapy
'''name=scrapy.Field()
    url=scrapy.Field()
    type=scrapy.Field()
    size=scrapy.Field()
    time=scrapy.Field
'''
from wangpan.items import WangpanItem
class wanSpider(scrapy.Spider):
    name = 'wangpang'
    allowed_domains=['panduoduo.net']
    start_urls=['http://www.panduoduo.net/c/4/{}'.format(n) for n in range(1,88764)]#
    def parse(self, response):
        #print(response.text)
        nodes_list=response.xpath('//table[@class="list-resource"]/tr')

        items=[]
        print(nodes_list)

        base_url='http://www.panduoduo.net'
        for node in nodes_list[1:]:
            item=WangpanItem()
            name=node.xpath('./td[@class="t1"]/a/text()').extract()[0]

            end_url=node.xpath('./td[@class="t1"]/a/@href').extract()


            url=base_url+''.join(end_url)
            type=node.xpath('./td/a[@class="tag"]/text()').extract()[0]
            size=node.xpath('./td[@class="t2"]/text()').extract()[0]
            time1=node.xpath('./td/span[@class="green"]/text()').extract()
            time2=node.xpath('./td[6]/text()').extract()
            print(time2)
            if len(time2)==2:
                time=''.join(time1)+time2[1]
            elif len(time2)==1:
                time=''.join(time1)+time2[0]
            else:pass
            item['name']=name
            item['url']=url
            item['type']=type
            item['size']=size
            item['time']=time
            items.append(item)
            yield  item


