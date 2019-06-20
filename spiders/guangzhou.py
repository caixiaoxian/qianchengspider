# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from qiancheng.items import QianchengItem
import ssl

class GuangzhouSpider(BaseSpider):
    name = 'guangzhou'
    # allowed_domains = ['https://search.51job.com/']
    #start_urls = ['http://https://search.51job.com//']
    start_urls = ['https://search.51job.com/list/030200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,1.html']
    def parse(self, response):
        # ssl._create_default_https_context=ssl._create_unverified_context()
       # print response.text
        selector=Selector(response)
        totaljob=selector.xpath('//div[@class="el"]')
        for eachjob in totaljob:
            # posi=eachjob.xpath('p/span/a/@title').extract()
            # print (pos)
            curlz=eachjob.xpath('//p/span/a/@href').extract()
            # print curl
            # print (curl)
            # curl="".join(curl) if curl else None
            # curl=curl[0] if curl else None
            # company1=eachjob.xpath('span[@class="t2"]/a/@title').extract()
            # #company=company[0]
            # area1=eachjob.xpath('span[@class="t3"]/text()').extract()
            # #area=area[0]
            # money1=eachjob.xpath('span[@class="t4"]/text()').extract()
            # #money=money[0]
            # date1=eachjob.xpath('span[@class="t5"]/text()').extract()
            # #date=date[0]

            item=QianchengItem()
            # item['curl']=curl
            # item['company']=company


            item['skill']=''
            item['walfare']=''
            item['job_db']=''
            print (type(curlz))
            # yield  item
        for curl in curlz:
            item['curl']=curl
            yield Request(curl,meta={'job':item},callback=self.parse_jobdetail,dont_filter=True)
            # yield Request(curl,meta={'job':item},callback=self.parse_jobdetail)
        nextlink=selector.xpath(u'//li[@class="bk"]/a[text()="下一页"]/@href').extract()
        if nextlink:
            nextlink=nextlink[0]
           # print "fff",nextlink
            yield Request(nextlink,callback=self.parse)

    def parse_jobdetail(self,response):
        selector=Selector(response)
        type=selector.xpath('//div[@class="com_tag"]/p[1]/@title').extract_first()
        population=selector.xpath('//div[@class="com_tag"]/p[2]/@title').extract_first()
        industry=selector.xpath('//div[@class="com_tag"]/p[3]/@title').extract_first()
        place1=selector.xpath('//div[@class="bmsg inbox"]/p/text()').extract()
        place=place1[1]
        pos=selector.xpath('//div[@class="cn"]/h1/text()').extract_first()
        money=selector.xpath('//div[@class="cn"]/strong/text()').extract_first()
        company=selector.xpath('//div[@class="cn"]/p[@class="cname"]/a/@title').extract_first()
        skill=selector.xpath('//div[@class="cn"]/p[@class="msg ltype"]/@title').extract_first()
        walfare=selector.xpath('//div[@class="cn"]//div[@class="t1"]/span/text()').extract_first()
        job_demand=selector.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract()
        job_db="".join(job_demand)
        item=response.meta['job']
        item['skill']=skill
        item['walfare']=walfare
        item['job_db']=job_db
        item['pos']=pos
        item['money']=money
        item['company']=company
        item['type']=type
        item['population']=population
        item['industry']=industry
        item['place']=place
        print (place)
     #item['job_db'
        yield item
