__author__ = 'Administrator'
from scrapy import cmdline
cmdline.execute("scrapy crawl review -o review.json -s FEED_EXPORT_ENCODING='utf-8'".split())