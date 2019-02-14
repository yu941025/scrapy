# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html




import pymysql

class SinaPipeline(object):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',user='root',password='123456',database='yuzhixiang', port=3306,charset='utf8') #创建连接
        self.cursor = self.conn.cursor()  #创建数据库游标

    def process_item(self, item, spider):
        sql1='select newsTitle from sina_news'
        self.cursor.execute(sql1)
        a=self.cursor.fetchall()

        if (item['newsTitle'],) in a:
            print('已存在')
        sql = 'insert into sina_news(newsTitle,newsUrl,newsTime,content) VALUES (%r,%r,%r,%r)'%(item['newsTitle'], item['newsUrl'], item['newsTime'], item['content'])
        self.cursor.execute(sql)  #执行sql语句
        self.conn.commit()  #提交
        return item

    def close_spider(self,spider):
        self.cursor.close() #关闭
        self.conn.close()
