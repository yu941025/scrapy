# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie':'_ntes_nuid=594dbe2f565353a16cb7ba59c4695b09; usertrack=ezq0pVqx02bBAFC1KrydAg==; _iuqxldmzr_=32; _ga=GA1.2.763136168.1521603242; WM_TID=nv1r28Tok%2BxFFBBUQUdtP06IJLcXFdbc; UM_distinctid=16754372e3c2c4-051e550172ec97-454c092b-1fa400-16754372e3d368; __gads=ID=f84cfc63c8bbcb65:T=1543306177:S=ALNI_MbbNAz92mexvXwjh5pN3uoFgDCttA; Province=0571; City=0571; vjuids=-6fa42ab97.167cf7c3656.0.560c5f3728a9; vjlast=1545374283.1545374283.30; _ntes_nnid=594dbe2f565353a16cb7ba59c4695b09,1545374283354; ne_analysis_trace_id=1545374283358; s_n_f_l_n3=9b102d7d92cb8f4a1545374283361; _antanalysis_s_id=1545374283761; vinfo_n_f_l_n3=9b102d7d92cb8f4a.1.2.1543306162773.1543392489266.1545374318611; hb_MA-BFF5-63705950A31C_source=www.so.com; __utmc=94650624; __utmz=94650624.1546566395.7.4.utmcsr=jqhtml.com|utmccn=(referral)|utmcmd=referral|utmcct=/13432.html; WM_NI=o1TOXmiun5Y%2FMIGmR1hwaftITBuQH%2F6WffEuCAHQE2wOTJu3ModIb3thFVmr9NHqQku%2FuYJpzwTi0suSRY3Mn0YxG6OMuIYLEBub3DIyj8BsoS0MZkrOq4HokwxTROi4dDk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1f960a1aebeb8eb3a8a9e8fb3d45b928e9f84f27d9786fcd2cc3bed9cbdace12af0fea7c3b92aadef9cb0db67ababa2d6dc258f97898ed13baca9af87f743989ebbb2cb25f689aa87c87f819f88b2c83ab5919cabf8398fb1acaae139b8b88ab7f07afb928892d461b7f1bbbac97cbaa99c8ab379b78d9ebab247aef09799c63e8d93bbaadc48879ebb83b2508ba7a6d9c179ad8d00aed961b291bfd5cb65a9a9b8b5d145abecaca5ea37e2a3; JSESSIONID-WYYY=n4%2B3Q7bpHOp%2FiDK6qabdtZwCo1zyXv5fY70V0u%2BbXbDkKpHkkgVDCaUw%2BlRix6sQ1SXI0R%2FpftUVvYgteo93VHEt2BPDM6sR6myvxc%2FZICfcEOOtpISnYafDxyY68ofhpph5yop8HJpiTCIxYnIc2fnQeM7EoMR5%2B3zUD%5C%2B7YBBuljAt%3A1546583864042; __utma=94650624.763136168.1521603242.1546573302.1546582322.9; MUSIC_U=9de0b492647e46614e4a4e07bebd1d3c79556da8755b09101eede7b639c2808e4601424faa412925fed95fc46eaee8d90ec7703fcbe15f2ba4e4eb26f0d98160f2f513a9c38b5dc7; __remember_me=true; __csrf=17ba0fe742198e584f7b42015018b064; __utmb=94650624.8.10.1546582322',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'


}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music163.middlewares.Music163SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music163.middlewares.Music163DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'music163.pipelines.MongoPipeline': 300,
}
# 添加数据库信息
MONGO_URI = 'localhost'
MONGO_DB = 'music163'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
