# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'youxiake'
    allowed_domains = ['youxiake.com']
    start_urls = ['http://www.youxiake.com/lines/list?code=around&place_id=2&days=1&month=0&holiday=0&price=0&tag=0&class_id=0&gts=0&gte=0&sdel=1&p=1']

    def parse(self, response):
        item = AutopjtItem()
        item["mingcheng"] = response.xpath('//h3[@class="yxk_dataList_title"]/a/text()').extract()
        item["yibaomingrenshu"] = response.xpath('//div[@class="yxk_dataList_info_bottom fn-clear"]/span[1]/text()').extract()
        item["price"] = response.xpath('//a[@class="yxk_dataList_info_price"]/text()[2]').extract()
        item["link"] = response.xpath('//a[@class="yxk_dataList_info_price"]/@href').extract()
        item["remark"] = response.xpath('//p[@class="yxk_dataList_msg"]/text()').extract()


        yield item
        for i in range(2, 8):
            url = "http://www.youxiake.com/lines/list?code=around&place_id=2&days=1&month=0&holiday=0&price=0&tag=0&class_id=0&gts=0&gte=0&sdel=1&p=" + str(i)
            yield Request(url, callback=self.parse)
