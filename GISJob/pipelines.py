# -*- coding: utf-8 -*-

# Define your item pipelines here
#插入爬取的一条岗位信息到MySQL数据库中
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors

class GisjobPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = 'localhost',
            db = 'test',
            user = 'root',
            passwd = '1234',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )
    def process_item(self, item, spider):
        item.setdefault('url', '')
        item.setdefault('job', '')
        item.setdefault('location', '')
        item.setdefault('salary', '')
        item.setdefault('ins', '')
        item.setdefault('instype', '')

        item.setdefault('jingyan', '')
        item.setdefault('xueli', '')
        item.setdefault('recruitnum', '')
        item.setdefault('releasetime', '')
        item.setdefault('language', '')
        item.setdefault('zhuanye', '')

        item.setdefault('labels', '')
        item.setdefault('jobinfo', '')
        item.setdefault('contactinfo', '')
        item.setdefault('insinfo', '')

        self.dbpool.runInteraction(self.inserttosql, item)
        return item
    def inserttosql(self, tx, item):
        tx.execute("insert into tb_gis_51job(url,job,location,salary,ins,instype,jingyan,xueli,recruitnum,releaseTime,language,zhuanye,labels,jobinfo,contactinfo,insinfo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (item['url'],item['job'],item['location'],item['salary'],item['ins'],item['instype'], item['jingyan'],item['xueli'],item['recruitnum'],item['releasetime'],item['language'],item['zhuanye'],item['labels'],item['jobinfo'],item['contactinfo'],item['insinfo'])
        )
