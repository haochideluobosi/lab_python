# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

import xlsxwriter


class AutopjtPipeline(object):
    def __init__(self):
        self.workbook = xlsxwriter.Workbook('youxiake.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.set_column('A:A', 20)
        bold = self.workbook.add_format({'bold': True})
        self.worksheet.write('A1', u'名称', bold)
        self.worksheet.write('B1', u'已报名人数', bold)
        self.worksheet.write('C1', u'价格', bold)
        self.worksheet.write('D1', u'链接', bold)
        self.worksheet.write('E1', u'备注', bold)
        self.row = 1
        pass

    def process_item(self, item, spider):
        text_wrap = self.workbook.add_format({'bold': False,
                                              'top': 2,  # 上边框，后面参数是线条宽度
                                              'left': 2,  # 左边框
                                              'right': 2,  # 右边框
                                              'bottom': 2,  # 底边框
                                              'text_wrap': 1})

        for j in range(0, len(item["mingcheng"])):
            mingcheng = item["mingcheng"][j]
            yibaomingrenshu = item["yibaomingrenshu"][j]
            price = item["price"][j]
            link = item["link"][j]
            remark = item["remark"][j]

            self.worksheet.write(self.row, 0, mingcheng, text_wrap)
            self.worksheet.write(self.row, 1, yibaomingrenshu, text_wrap)
            self.worksheet.write(self.row, 2, price, text_wrap)
            self.worksheet.write(self.row, 3, link, text_wrap)
            self.worksheet.write(self.row, 4, remark, text_wrap)
            self.row = self.row + 1

        return item

    def close_spider(self, spider):
        print("close_spider")
        self.workbook.close()
