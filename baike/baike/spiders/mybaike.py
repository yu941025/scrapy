__author__ = 'Administrator'
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from baike.items import BaikeItem

class MybaikeSpider(CrawlSpider):
    name = 'mybaike'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.qichacha.com/firm_0374f43450839802afe38ada8335d1ca.html']
    cookie='UM_distinctid=164ac464663684-0c45d10a218b76-6b1b1279-1fa400-164ac46466445c; _uab_collina=153189864418983364687806; zg_did=%7B%22did%22%3A%20%22164ac46467a4c-074a653cae150f-6b1b1279-1fa400-164ac46467b788%22%7D; _umdata=2BA477700510A7DF036903FD88251246397949A3915B1548A7F13EFDA0976151C83D1E6CCEC052ABCD43AD3E795C914C2613C8A6BCBBE3C1640EF22CB028F6A3; saveFpTip=true; QCCSESSID=16g5ik9bk689b1pptcq9lcqc65; acw_tc=7ae4019a15469316652264363e7b9c52c421e8b7e6f528a78dcc9093cd; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1546931658,1546938207,1547016292,1547019293; CNZZDATA1254842228=794487190-1531893686-null%7C1547014711; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201547019292819%2C%22updated%22%3A%201547019577248%2C%22info%22%3A%201546931656713%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.so.com%22%2C%22cuid%22%3A%20%223207f097ce634f07ebfdd8f284e74a48%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1547019577'
    c=cookie.split(':')
    q=[i.split('=') for i in c]
    l={}
    for j in q:
        l


    rules = [Rule(LinkExtractor(allow=('https://www.qichacha.com/firm_(.*?).html')),callback='getParse',follow=True)]


    def getParse(self, response):
        name=response.xpath('//*[@id="company-top"]/div[2]/div[2]/div[1]/h1/text()').extract()
        #phone=response.xpath('//span[@class="cvlu"]/span/text()').extract()
        #email=response.xpath('//span[@class="cvlu"]/span/a/text()').extract()
        #diqu=response.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[11]/td[2]/text()').extract
        #jyfangwei=response.xpath('//*[@id="Cominfo"]/table/tbody/tr[11]/td/text()').extract()
        item = BaikeItem()
        item['name'] = name
        '''item['diqu'] = diqu
        item['email'] = email
        item['phone']=phone
        item['jyfangwei']=jyfangwei'''
        yield item
