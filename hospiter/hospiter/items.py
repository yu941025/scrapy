# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HospiterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hospitalName=scrapy.Field()
    hospitalSize=scrapy.Field()
    hospitalAddress=scrapy.Field()
    hospitalDesc=scrapy.Field()
