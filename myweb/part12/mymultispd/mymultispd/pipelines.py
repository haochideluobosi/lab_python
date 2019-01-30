# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class MymultispdPipeline(object):
    def __init__(self):
        self.file = codecs.open("D:/python35/myweb/part13/mydata1.json", 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        i = json.dumps(dict(item))
        line = i + '\n'
        print(line)
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
