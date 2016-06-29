# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from GISJob.items import GisjobItem

class GisjobSpider(scrapy.Spider):
    name = "gisjobspider"
    start_urls = []
    for i in range(1, 95):
        url = "http://search.51job.com/list/000000,000000,0000,00,9,99,gis,2,"+str(i)+".html"
        start_urls.append(url)

    def parse(self, response):
		print response.url 
		div = response.xpath("//div[@class='dw_table']/div[@class='el']")
		job = div.xpath(".//p/span/a/@title").extract()
		ins = div.xpath(".//span[@class='t2']/a/@title").extract()
		location = div.xpath(".//span[@class='t3']/text()").extract()
		salary = []
		t = div.xpath(".//span[@class='t4']").extract()
		for i in range(0, len(t)):
			salary.append(t[i][17: -7])
		releasetime = div.xpath(".//span[@class='t5']/text()").extract()
		items = []
		for i in range(0, len(div)):
			item = GisjobItem()
			item['job'] = job[i]
			item['ins'] = ins[i]
			item['location'] = location[i]
			item['salary'] = salary[i]
			item['releasetime'] = releasetime[i]
			items.append(item)
		return items


