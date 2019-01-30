# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    mingcheng = scrapy.Field()
    chuanyuefangshi = scrapy.Field()
    tubujuli = scrapy.Field()
    leijipashen = scrapy.Field()
    fengjingzhishu = scrapy.Field()
    huodongqiangdu = scrapy.Field()
    lianjiedizhi = scrapy.Field()
    yibaomingrenshu = scrapy.Field()
    pass