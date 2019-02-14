__author__ = 'Administrator'
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='123456',database='yuzhixiang', port=3306,charset='utf8')
cursor=conn.cursor()
sql='select newsTitle from sina_news '
cursor.execute(sql)
a=cursor.fetchall()
print(a)
