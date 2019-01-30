# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://blog.csdn.net/foruok/article/details/73076448',
    )
    urls2 = ("http://blog.csdn.net")

    def start_requests(self):
        for url in self.urls2:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath("/html/head/title/text()")
        print(item['urlname'])
        pass
