__author__ = 'Administrator'
from scrapy import cmdline
cmdline.execute('scrapy crawl mybaike  -o a.json -s FEED_EXPORT_ENCODING=UTF-8'.split())