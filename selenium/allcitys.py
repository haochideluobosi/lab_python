# -*- coding: UTF-8 -*-
import collections

import xlsxwriter
from selenium import webdriver


def get_not_null_val(dict, name):
    if name not in dict.keys():
        return ""
    return dict[name]


def get_not_null_detail(dict, name):
    if name not in dict.keys():
        dict[name] = {}
    return dict[name]


def set_detail(detail, name, value):
    if name in detail and detail[name] != value:
        # detail[name] = detail[name] + ";" + value
        print("origin:" + detail[name] + ",now:" + value)
        pass
    else:
        detail[name] = value


def wuba(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('http://www.58.com/changecity.html')
    level_1s = browser.find_elements_by_xpath('//*[@id="content-box"]/div[@class="content-letter"]')
    level_1s2 = browser.find_elements_by_xpath('//*[@id="hot"]')
    level_1s.extend(level_1s2)

    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.text);
            set_detail(detail, 'wuba', level_2.get_property('href'))
    try:
        print("58 OK!")
    finally:
        browser.quit()


def ganji(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('http://www.ganji.com/index.htm')
    level_1s = browser.find_elements_by_xpath('/html/body/div[1]/div[3]/dl/dd')
    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.text);
            set_detail(detail, 'ganji', level_2.get_property('href'))
    try:
        print("ganji OK!")
    finally:
        browser.quit()


def fangtianxia(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('http://www.fang.com/SoufunFamily.htm')
    level_1s = browser.find_elements_by_xpath('//div[@class="outCont"]//table[@class="table01"]//tr')
    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.get_attribute('text'));
            set_detail(detail, 'fangtianxia', level_2.get_property('href'))

    try:
        print("fangtianxia OK!")
    finally:
        browser.quit()


def anjuke(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('https://www.anjuke.com/sy-city.html')
    level_1s = browser.find_elements_by_xpath('//div[@class="city_list"]')
    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.get_attribute('text'));
            set_detail(detail, 'anjuke', level_2.get_property('href'))

    try:
        print("anjuke OK!")
    finally:
        browser.quit()


def kuaidian8(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('http://www.qd8.com.cn/')
    level_1s = browser.find_elements_by_xpath('//div[@class="citylist"]')
    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.get_attribute('text'));
            set_detail(detail, 'kuaidian8', level_2.get_property('href'))

    try:
        print("kuaidian8 OK!")
    finally:
        browser.quit()


def house365(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('http://sh.house365.com/')
    level_1s = browser.find_elements_by_xpath('//div[@class="smcom_select_drop"]//dl[@class="clearfix"]')
    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.get_attribute('text'));
            set_detail(detail, 'house365', level_2.get_property('href'))

    try:
        print("house365 OK!")
    finally:
        browser.quit()


def baixing(dict):
    chromedriver = "D:/Software/selenium/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    browser.get('http://www.baixing.com/?changeLocation=yes')
    level_1s = browser.find_elements_by_xpath('//ul[@class="wrapper"]')
    for level_1 in level_1s:
        level_2s = level_1.find_elements_by_tag_name('a')
        for level_2 in level_2s:
            detail = get_not_null_detail(dict, level_2.get_attribute('text'));
            set_detail(detail, 'baixing', level_2.get_property('href'))

    try:
        print("baixing OK!")
    finally:
        browser.quit()


def fangduoduo(dict):
    try:
        chromedriver = "D:/Software/selenium/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get('http://shanghai.fangdd.com/')
        level_1s = browser.find_elements_by_xpath('//ul[@class="_1oKQR"]')
        for level_1 in level_1s:
            level_2s = level_1.find_elements_by_tag_name('a')
            for level_2 in level_2s:
                detail = get_not_null_detail(dict, level_2.get_attribute('text'));
                set_detail(detail, 'fangduoduo', level_2.get_property('href'))

        print("fangduoduo OK!")
    finally:
        browser.quit()


def gerenfangyuanwang(dict):
    try:
        chromedriver = "D:/Software/selenium/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get('http://www.grfy.net/index.htm')
        level_1s = browser.find_elements_by_xpath('//div[@id="area-list"]//dd')
        for level_1 in level_1s:
            level_2s = level_1.find_elements_by_tag_name('a')
            for level_2 in level_2s:
                detail = get_not_null_detail(dict, level_2.get_attribute('text'));
                set_detail(detail, 'gerenfangyuanwang', level_2.get_property('href'))

        print("gerenfangyuanwang OK!")
    finally:
        browser.quit()


def diyishijianfangyuanwang(dict):
    try:
        chromedriver = "D:/Software/selenium/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get('http://www.01fy.cn/index.htm')
        level_1s = browser.find_elements_by_xpath('//div[@id="area-list"]//dd')
        for level_1 in level_1s:
            level_2s = level_1.find_elements_by_tag_name('a')
            for level_2 in level_2s:
                detail = get_not_null_detail(dict, level_2.get_attribute('text'));
                set_detail(detail, 'diyishijianfangyuanwang', level_2.get_property('href'))

        print("diyishijianfangyuanwang OK!")
    finally:
        browser.quit()


def tuitui99(dict):
    try:
        chromedriver = "D:/Software/selenium/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get('http://www.tuitui99.com/')
        level_1s = browser.find_elements_by_xpath('//div[@class="w_1200"]')
        for level_1 in level_1s:
            level_2s = level_1.find_elements_by_tag_name('a')
            for level_2 in level_2s:
                detail = get_not_null_detail(dict, level_2.get_attribute('text').strip());
                set_detail(detail, 'tuitui99', level_2.get_property('href'))

        print("tuitui99 OK!")
    finally:
        browser.quit()


def jinti(dict):
    try:
        chromedriver = "D:/Software/selenium/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get('http://www.jinti.com/fangchan/selectcity/')
        level_1s = browser.find_elements_by_xpath('//div[@class="mBox zoom a-z "]//dd')
        for level_1 in level_1s:
            level_2s = level_1.find_elements_by_tag_name('a')
            for level_2 in level_2s:
                detail = get_not_null_detail(dict, level_2.get_attribute('text').strip());
                set_detail(detail, 'jinti', level_2.get_property('href'))

        print("jinti OK!")
    finally:
        browser.quit()


def fangchanchaoshi(dict):
    try:
        chromedriver = "D:/Software/selenium/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get('http://www.fccs.com/city.html')
        level_1s = browser.find_elements_by_xpath('//div[@id="pro"]//dd')
        for level_1 in level_1s:
            level_2s = level_1.find_elements_by_tag_name('a')
            for level_2 in level_2s:
                detail = get_not_null_detail(dict, level_2.get_attribute('text').strip());
                set_detail(detail, 'fangchanchaoshi', level_2.get_property('href'))

        print("fangchanchaoshi OK!")
    finally:
        browser.quit()


def writeExcel(dict):
    workbook = xlsxwriter.Workbook('citys.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    row = 0

    worksheet.write(row, 0, u'city', bold)
    worksheet.write(row, 1, u'wuba_base_url', bold)
    worksheet.write(row, 2, u'wuba_chuzu_url')
    worksheet.write(row, 3, u'wuba_chushou_url')
    worksheet.write(row, 4, u'ganji_base_url', bold)
    worksheet.write(row, 5, u'ganji_chuzu_url', bold)
    worksheet.write(row, 6, u'ganji_chushou_url', bold)
    worksheet.write(row, 7, u'baixing_base_url', bold)
    worksheet.write(row, 8, u'baixing_chuzu_url', bold)
    worksheet.write(row, 9, u'baixing_chushou_url', bold)
    worksheet.write(row, 10, u'anjuke_base_url', bold)
    worksheet.write(row, 11, u'anjuke_chuzu_url', bold)
    worksheet.write(row, 12, u'geren_base_url', bold)
    worksheet.write(row, 13, u'geren_chuzu_url', bold)
    worksheet.write(row, 14, u'geren_chushou_url', bold)
    worksheet.write(row, 15, u'fangtianxia_base_url', bold)
    worksheet.write(row, 16, u'fangtianxia_chuzu_url', bold)
    worksheet.write(row, 17, u'fangtianxia_chushou_url', bold)
    worksheet.write(row, 18, u'diyishijian_base_url', bold)
    worksheet.write(row, 19, u'diyishijian_chuzu_url', bold)
    worksheet.write(row, 20, u'diyishijian_chushou_url', bold)
    worksheet.write(row, 21, u'house365_base_url', bold)
    worksheet.write(row, 22, u'house365_chuzu_url', bold)
    worksheet.write(row, 23, u'house365_chushou_url', bold)
    worksheet.write(row, 24, u'kuaidian8_base_url', bold)
    worksheet.write(row, 25, u'kuaidian8_chuzu_url', bold)
    worksheet.write(row, 26, u'kuaidian8_chushou_url', bold)
    worksheet.write(row, 27, u'tuitui99_base_url', bold)
    worksheet.write(row, 28, u'tuitui99_chuzu_url', bold)
    worksheet.write(row, 29, u'tuitui99_chushou_url', bold)
    worksheet.write(row, 30, u'jinti_base_url', bold)
    worksheet.write(row, 31, u'jinti_chuzu_url', bold)
    worksheet.write(row, 32, u'jinti_chushou_url', bold)
    worksheet.write(row, 33, u'fangchanchaoshi_base_url', bold)
    worksheet.write(row, 34, u'fangchanchaoshi_chuzu_url', bold)
    worksheet.write(row, 35, u'fangchanchaoshi_chushou_url', bold)

    for key in dict:
        detail = dict[key]
        row = row + 1
        worksheet.write(row, 0, key)
        if get_not_null_val(detail, 'wuba'):
            worksheet.write(row, 1, get_not_null_val(detail, 'wuba'))
            worksheet.write(row, 2, get_not_null_val(detail, 'wuba') + 'chuzu/0/pn{}/')
            worksheet.write(row, 3, get_not_null_val(detail, 'wuba') + 'ershoufang/0/pn{}/')
        if get_not_null_val(detail, 'ganji'):
            worksheet.write(row, 4, get_not_null_val(detail, 'ganji'))
            worksheet.write(row, 5, get_not_null_val(detail, 'ganji') + 'fang1/a1o{}P99/')
            worksheet.write(row, 6, get_not_null_val(detail, 'ganji') + 'fang5/a1o{}/')
        if get_not_null_val(detail, 'baixing'):
            worksheet.write(row, 7, get_not_null_val(detail, 'baixing'))
            worksheet.write(row, 8, get_not_null_val(detail, 'baixing') + 'zhengzu/?grfy=1&page={}&sortKey=createdTime')
            worksheet.write(row, 9,
                            get_not_null_val(detail, 'baixing') + 'ershoufang/?grfy=1&page={}&sortKey=createdTime')
        if get_not_null_val(detail, 'anjuke'):
            worksheet.write(row, 10, get_not_null_val(detail, 'anjuke'))
            worksheet.write(row, 11, get_not_null_val(detail, 'anjuke').replace('anjuke.com',
                                                                                'zu.anjuke.com') + 'fangyuan/l2-p{}-px3/')
        if get_not_null_val(detail, 'gerenfangyuanwang'):
            worksheet.write(row, 12, get_not_null_val(detail, 'gerenfangyuanwang'))
            worksheet.write(row, 13,
                            get_not_null_val(detail, 'gerenfangyuanwang') + 'rent/list_2_0_0_0-0_0_0-0_0_2_0_{}_.html')
            worksheet.write(row, 14,
                            get_not_null_val(detail, 'gerenfangyuanwang') + 'sale/list_2_0_0_0-0_0_0-0_0_2_0_{}_.html')

        if get_not_null_val(detail, 'fangtianxia'):
            worksheet.write(row, 15, get_not_null_val(detail, 'fangtianxia'))
            if key == "北京":
                worksheet.write(row, 16, 'http://zu.fang.com/' + 'house/a21-h316-i3{}/')
                worksheet.write(row, 17, 'http://esf.fang.com/' + 'house/a211-h316-i3{}/')
            elif key == '绍兴':
                worksheet.write(row, 16, "http://zu.shaoxing.fang.com/house/a21-h316-i3{}")
                worksheet.write(row, 17, get_not_null_val(detail, 'fangtianxia').replace('http://',
                                                                                         'http://esf.') + 'house/a211-h316-i3{}/')
            else:
                worksheet.write(row, 16, get_not_null_val(detail, 'fangtianxia').replace('http://',
                                                                                         'http://zu.') + 'house/a21-h316-i3{}/')
                worksheet.write(row, 17, get_not_null_val(detail, 'fangtianxia').replace('http://',
                                                                                         'http://esf.') + 'house/a211-h316-i3{}/')
        if get_not_null_val(detail, 'diyishijianfangyuanwang'):
            worksheet.write(row, 18, get_not_null_val(detail, 'diyishijianfangyuanwang'))
            worksheet.write(row, 19, get_not_null_val(detail,
                                                      'diyishijianfangyuanwang') + 'rent/list_2_0_0_0-0_0_0-0_0_0_0_0_0_0_2_0_{}_.html')
            worksheet.write(row, 20, get_not_null_val(detail,
                                                      'diyishijianfangyuanwang') + 'sale/list_2_0_0_0-0_0_0-0_0_0_0-0_0_0-0_2_0_{}_.html')
        if get_not_null_val(detail, 'house365'):
            worksheet.write(row, 21, get_not_null_val(detail, 'house365'))
            if key == '南京':
                worksheet.write(row, 22, get_not_null_val(detail, 'house365').replace('house365.com/index.html',
                                                                                      'rent.house365.com/') + 'district_i1/dl_n8-p{}.html')
            elif key == '西安':
                worksheet.write(row, 22, get_not_null_val(detail, 'house365').replace('house365.com/index.html',
                                                                                      'rent.house365.com/') + 'district_i1/dl_n2-p{}.html')
            else:
                worksheet.write(row, 22, get_not_null_val(detail, 'house365').replace('house365.com/index.html',
                                                                                      'rent.house365.com/') + 'district_i1/dl_n9-p{}.html')
            worksheet.write(row, 23, get_not_null_val(detail, 'house365').replace('house365.com/index.html',
                                                                                  'sell.house365.com/') + 'district_i1/dl_n11-p{}.html')
        if get_not_null_val(detail, 'kuaidian8'):
            worksheet.write(row, 24, get_not_null_val(detail, 'kuaidian8'))
            worksheet.write(row, 25, get_not_null_val(detail, 'kuaidian8') + 'gerenchuzu/p{}/')
            worksheet.write(row, 26, get_not_null_val(detail, 'kuaidian8') + 'ershoufang/p{}/')
        if get_not_null_val(detail, 'tuitui99'):
            worksheet.write(row, 27, get_not_null_val(detail, 'tuitui99'))
            worksheet.write(row, 28, get_not_null_val(detail, 'tuitui99') + 'grrent/px7/p{}.html')
            worksheet.write(row, 29, get_not_null_val(detail, 'tuitui99') + 'grsale/px7/p{}.html')
        if get_not_null_val(detail, 'jinti'):
            worksheet.write(row, 30, get_not_null_val(detail, 'jinti'))
            worksheet.write(row, 31, get_not_null_val(detail, 'jinti').replace('fangchan/', 'zufang/i1p{}.htm'))
            worksheet.write(row, 32, get_not_null_val(detail, 'jinti').replace('fangchan/', 'ershoufang/i1p{}.htm'))
        if get_not_null_val(detail, 'fangchanchaoshi'):
            worksheet.write(row, 33, get_not_null_val(detail, 'fangchanchaoshi'))
            worksheet.write(row, 34, get_not_null_val(detail, 'fangchanchaoshi').replace('http://',
                                                                                         'http://rent.') + 'lease/search/fr1_or11_so5_p{}.html')
            worksheet.write(row, 35, get_not_null_val(detail, 'fangchanchaoshi').replace('http://',
                                                                                         'http://second.') + 'sale/search/or11_p{}.html')
    print("workbook OK!")
    workbook.close()


# def read_excel(dict):
#     # 文件位置
#     excelFile = xlrd.open_workbook(u'C:\\Users\\gong.hua\\Desktop\\采房.xlsx')
#     sheet = excelFile.sheet_by_name(u'城市&&通用网站-个人-住宅')
#     newDict = collections.OrderedDict()
#     for i in range(3, 100):
#         for j in range(1, 2):
#             newDict[sheet.cell_value(i, j)] = get_not_null_detail(dict, sheet.cell_value(i, j))
#
#     return newDict

dict = collections.OrderedDict()  # = {u"北京":{"city_58":"http://58"}}
# house365
house365(dict)
# 58同城
wuba(dict)
# 赶集网
ganji(dict)
# 百姓网
baixing(dict)
# 安居客
anjuke(dict)
# 个人房源网
gerenfangyuanwang(dict)
# 房天下
fangtianxia(dict)
# 第1时间房源网
diyishijianfangyuanwang(dict)

# #快点8
kuaidian8(dict)

tuitui99(dict)
jinti(dict)
fangchanchaoshi(dict)
writeExcel(dict)
