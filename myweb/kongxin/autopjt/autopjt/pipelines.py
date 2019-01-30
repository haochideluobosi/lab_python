# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

import xlsxwriter


class AutopjtPipeline(object):
    def __init__(self):
        self.workbook = xlsxwriter.Workbook('kongxin.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.set_column('A:A', 20)
        bold = self.workbook.add_format({'bold': True})
        self.worksheet.write('A1', u'名称', bold)
        self.worksheet.write('B1', u'风景指数', bold)
        self.worksheet.write('C1', u'活动强度', bold)
        self.worksheet.write('D1', u'徒步距离', bold)
        self.worksheet.write('E1', u'累计爬升', bold)
        self.worksheet.write('F1', u'穿越方式', bold)
        self.worksheet.write('G1', u'链接', bold)
        self.worksheet.write('H1', u'已报名人数', bold)
        self.row = 1
        self.max = 20
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
            if mingcheng == '提示信息  ':
                return item
            chuanyuefangshi = ''
            fengjingzhishu = ''
            huodongqiangdu = ''
            tubujuli = ''
            leijipashen = ''
            lianjiedizhi = ''
            yibaomingrenshu = ''
            if item["chuanyuefangshi"]:
                chuanyuefangshi = item["chuanyuefangshi"][j]
                if chuanyuefangshi:
                    chuanyuefangshi = chuanyuefangshi.replace('穿越方式：', '')
            if item["tubujuli"]:
                tubujuli = item["tubujuli"][j]
                if tubujuli:
                    tubujuli = tubujuli.replace('徒步距离：', '')
            if item["leijipashen"]:
                leijipashen = item["leijipashen"][j]
                if leijipashen:
                    leijipashen = leijipashen.replace('累计爬升：', '')
            if item["fengjingzhishu"]:
                fengjingzhishu = item["fengjingzhishu"][j]
                if fengjingzhishu:
                    fengjingzhishu = fengjingzhishu.replace('风景指数：', '')
            if item["huodongqiangdu"]:
                huodongqiangdu = item["huodongqiangdu"][j]
                if huodongqiangdu:
                    huodongqiangdu = huodongqiangdu.replace('活动强度：', '')
            if item["yibaomingrenshu"]:
                yibaomingrenshu = item["yibaomingrenshu"][j]
                if yibaomingrenshu:
                    yibaomingrenshu = yibaomingrenshu.replace('已报名人数：', '')
                else:
                    return item
            lianjiedizhi = item["lianjiedizhi"][j]
            self.worksheet.write(self.row, 0, mingcheng, text_wrap)
            self.worksheet.write(self.row, 1, fengjingzhishu, text_wrap)
            self.worksheet.write(self.row, 2, huodongqiangdu, text_wrap)
            self.worksheet.write(self.row, 3, tubujuli, text_wrap)
            self.worksheet.write(self.row, 4, leijipashen, text_wrap)
            self.worksheet.write(self.row, 5, chuanyuefangshi, text_wrap)
            self.worksheet.write(self.row, 6, lianjiedizhi, text_wrap)
            self.worksheet.write(self.row, 7, yibaomingrenshu, text_wrap)

        self.row = self.row + 1
        return item

    def close_spider(self, spider):
        print("close_spider")
        self.workbook.close()
