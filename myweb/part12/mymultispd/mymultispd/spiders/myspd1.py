# -*- coding: utf-8 -*-
import scrapy
from mymultispd.items import MyfirstpjtItem


class Myspd1Spider(scrapy.Spider):
    name = 'myspd1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.csdn.net/foruok/article/details/73076448']

    def parse(self, response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath("/html/head/title/text()")
        print(item['urlname'])
        pass
