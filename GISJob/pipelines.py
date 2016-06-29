# -*- coding: utf-8 -*-

# Define your item pipelines here
#
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
        item.setdefault('job', '')
        item.setdefault('ins', '')
        item.setdefault('location', '')
        item.setdefault('salary', '')
        item.setdefault('releasetime', '')
        self.dbpool.runInteraction(self.inserttosql, item)
        return item

    def inserttosql(self, tx, item):
        tx.execute("insert into tb_gis_51job(Job, Ins, Location, Salary, ReleaseTime) values(%s,%s,%s,%s,%s)",
                   (item['job'], item['ins'], item['location'], item['salary'], item['releasetime'])
        )
