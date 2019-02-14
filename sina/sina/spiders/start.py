__author__ = 'Administrator'
def main():
    from scrapy import cmdline
    cmdline.execute('scrapy crawl mysina -o a.json'.split())
if __name__=='__main__':
    main()