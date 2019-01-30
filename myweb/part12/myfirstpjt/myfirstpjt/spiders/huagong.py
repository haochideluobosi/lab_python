# -*- coding: utf-8 -*-
import scrapy


class HuagongSpider(scrapy.Spider):
    name = 'huagong'
    allowed_domains = ['http://blog.csdn.net']
    start_urls = ['http://http://blog.csdn.net/']

    def parse(self, response):
        pass
