# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from scrapy.conf import settings
class WangpanPipeline(object):
    def process_item(self, item, spider):
        return item
class MongoPipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient(host=settings['MONGO_HOST'],port=settings['MONGO_PORT'])
        self.datebase=self.client[settings['MONGO_DATABASE']]
        self.collection=self.datebase[settings['MONGO_COLLECTION']]
    def process_item(self,item,spider):
        postItem=dict(item)
        self.collection.insert(postItem)
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file=open('ceshi.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        message=str(item)

        self.file.write(message+'\n')
        return item
    def close_spider(self,spider):
        self.file.close()
