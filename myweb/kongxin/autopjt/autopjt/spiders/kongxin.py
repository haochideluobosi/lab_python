# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'kongxin'
    allowed_domains = ['kxhuwai.com']
    start_urls = ['http://www.kxhuwai.com/thread-3390-1-1.html']

    def parse(self, response):
        item = AutopjtItem()
        item["mingcheng"] = response.xpath('//title/text()').extract()
        item["chuanyuefangshi"] = response.xpath(u'//*[contains(text(), "穿越方式：")]/text()').extract()
        item["tubujuli"] = response.xpath(u'//*[contains(text(), "徒步距离：")]/text()').extract()
        item["leijipashen"] = response.xpath(u'//*[contains(text(), "累计爬升：")]/text()').extract()
        item["fengjingzhishu"] = response.xpath(u'//*[contains(text(), "风景指数：")]/text()').extract()
        item["huodongqiangdu"] = response.xpath(u'//*[contains(text(), "活动强度：")]/text()').extract()
        item["lianjiedizhi"] = response.xpath('//link[1]/@href').extract()
        item["yibaomingrenshu"] = response.xpath(u'//dl[@class="nums mtw"]/dd/em/text()').extract()

        yield item
        for i in range(3391, 3470):
            url = "http://www.kxhuwai.com/thread-" + str(i) + "-1-1.html"
            yield Request(url, callback=self.parse)
