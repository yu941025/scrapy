__author__ = 'Administrator'
from scrapy import cmdline
cmdline.execute("scrapy crawl music -o review.json".split())
cmdline.execute("scrapy crawl video -o video.json".split())