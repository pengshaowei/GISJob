# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from GISJob.items import GisjobItem

class GisjobSpider(scrapy.Spider):
    name = "gisjobspider"
    start_urls = []
    for i in range(1, 95):
        url = "http://search.51job.com/list/000000,000000,0000,00,9,99,GIS,2,"+str(i)+".html"
        start_urls.append(url)

    def parse(self, response):
		div = response.xpath("//div[@class='dw_table']/div[@class='el']")
		joburllist = div.xpath(".//p/span/a/@href").extract()
		for joburl in joburllist:
			yield scrapy.Request(url=joburl,callback=self.parse_item)

    def parse_item(self,response):
		item = GisjobItem()
		item['url'] = response.url
		print "URL:"+response.url
		#包括job， location， salary， ins, instype
		divcn = response.xpath("//div[@class='cn']")
		if len(divcn)==0:
			print "-----------------------------------------------------------------JOB-STOP--"
			return item
		job = divcn.xpath(".//h1/@title").extract()[0]
		location = divcn.xpath(".//span[@class='lname']/text()").extract()[0]
		salary = divcn.xpath(".//strong").extract()[0]
		salary = salary[8:-9]
		#todo salary中可能为空
		ins = divcn.xpath(".//p[@class='cname']/a/@title").extract()[0]
		instypels = divcn.xpath(".//p[@class='msg ltype']/text()").extract()[0].encode('utf-8', 'ignore').split("|")
		instype = ''
		for i in instypels:
			instype += i.strip()+'|'
		instype=instype[:-1]
		#爬取 div class=t1 中的六项内容
		jingyan = ''
		xueli = ''
		recruitnum = ''
		releasetime = ''
		language = ''
		zhuanye = ''
		info = {'i1':'jingyan','i2':'xueli','i3':'recruitnum','i4':'releasetime','i5':'language','i6':'zhuanye'}
		span = response.xpath("//div[@class='t1']/span")
		for i in range(0,len(span)):
			emc = span[i].xpath(".//em/@class").extract()[0]
			#妈的要是有switch就好了
			if info[emc]=='jingyan':
				jingyan = span[i].xpath(".//text()").extract()[0]
			if info[emc]=='xueli':
				xueli = span[i].xpath(".//text()").extract()[0]
			if info[emc]=='recruitnum':
				recruitnum = span[i].xpath(".//text()").extract()[0]
			if info[emc]=='releasetime':
				releasetime = span[i].xpath(".//text()").extract()[0]
			if info[emc]=='language':
				language = span[i].xpath(".//text()").extract()[0]
			if info[emc]=='zhuanye':
				zhuanye = span[i].xpath(".//text()").extract()[0]

		labels = ''
		divinbox = response.xpath("//div[@class='jtag inbox']")
		labells =divinbox.xpath(".//p[@class='t2']/span/text()").extract()
		if len(labells)!=0:
			for lable in labells:
				labels += lable+'-'
		labels=labels[:-1]
		jobinfo = ''
		jobinfols = response.xpath("//div[@class='bmsg job_msg inbox']//text()").extract()
		if len(jobinfols)!=0:
			for text in jobinfols:
				jobinfo += text
		contactinfo = ''
		bmsg = response.xpath("//div[@class='bmsg inbox']/p")
		contactinfols = bmsg.xpath(".//span/text()|.//text()").extract()
		if len(contactinfols)!=0:
			for k in contactinfols:
				contactinfo += k
		insinfo = ''
		insinfols = response.xpath("//div[@class='tmsg inbox']/text()").extract()
		if len(contactinfols)!=0:
			for l in insinfols:
				insinfo += l


		item['job'] = job
		item['location'] = location
		item['salary'] = salary
		item['ins'] = ins
		item['instype'] = instype

		item['jingyan'] = jingyan
		item['xueli'] = xueli
		item['recruitnum'] = recruitnum
		item['releasetime'] = releasetime
		item['language'] = language
		item['zhuanye'] = zhuanye

		item['labels'] = labels
		item['jobinfo'] = jobinfo
		item['contactinfo'] = contactinfo
		item['insinfo'] = insinfo

		print response.url+"FINISHED:"
		return item