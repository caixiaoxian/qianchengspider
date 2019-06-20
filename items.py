# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class QianchengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pos=Field()
    curl=Field()
    company=Field()
    area=Field()
    money=Field()
    date=Field()
    skill=Field()
    walfare=Field()
    job_db=Field()
    type=Field()
    population=Field()
    industry=Field()
    place=Field()

