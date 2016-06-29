# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GisjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    job = scrapy.Field()
    ins = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    releasetime = scrapy.Field()

    pass
