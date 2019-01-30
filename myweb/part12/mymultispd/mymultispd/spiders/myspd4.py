# -*- coding: utf-8 -*-
import scrapy


class Myspd4Spider(scrapy.Spider):
    name = 'myspd4'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
