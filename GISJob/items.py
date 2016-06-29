# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GisjobItem(scrapy.Item):
	url = scrapy.Field()
	job = scrapy.Field()	#岗位名称
	location = scrapy.Field()	#工作地点
	salary = scrapy.Field()	#薪资
	ins = scrapy.Field()	#公司名称
	instype = scrapy.Field()	#公司类型

	jingyan = scrapy.Field()	#经验要求
	xueli = scrapy.Field()	#学历要求
	recruitnum = scrapy.Field()	#招收人数
	releasetime = scrapy.Field()	#发布时间
	language = scrapy.Field()	#语言能力要求
	zhuanye = scrapy.Field()	#专业要求

	labels = scrapy.Field()	#岗位福利标签

	jobinfo = scrapy.Field()	#岗位详细信息
	contactinfo = scrapy.Field()	#联系方式
	insinfo = scrapy.Field()	#公司信息


	
	
