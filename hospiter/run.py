__author__ = 'Administrator'
from scrapy import cmdline
cmdline.execute('scrapy crawl hospital -o 456.json'.split())