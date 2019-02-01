from selenium import webdriver
from urllib import request
from bs4 import BeautifulSoup
import xlrd


def read_excel(dict):
    # 文件位置
    excelFile = xlrd.open_workbook('citys.xlsx')
    sheet = excelFile.sheet_by_name('Sheet1')
    for i in range(3, 100):
        for j in range(1, 2):
            cellval = sheet.cell_value(i, j)



urls = ["http://renhuaishi.58.com/chuzu/0"]
url = "http://sh.58.com/chuzu/0/pn0"
# 模拟真实浏览器进行访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read()
page_info = page_info.decode('utf-8')
# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')

# 以格式化的形式打印html
# print(soup.prettify())
# href = soup.select_one('div.des h2 a').get('href')  # 查找所有a标签中class='title'的语句
href = soup.select_one('.des a[tongji_label]').get('href')
print(href)

page2 = request.Request("http:" + href, headers=headers)
page2_info = request.urlopen(page2).read()
page2_info = page2_info.decode('utf-8')
soup2 = BeautifulSoup(page2_info, 'html.parser')
text = soup2.select_one('#single .agent-name.f16.pr .c_000').text
print(text)

text = soup2.select_one('.house-pay-way.f16 .c_333').text
print(text)
text = soup2.select_one('#leftImg').text
print(text)
