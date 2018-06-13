import urllib.request
from bs4 import BeautifulSoup
import xlwt

addressHome = 'https://www.ebay.com.au/b/Womens-Sunglasses/45246/bn_1843392?LH_BIN=1&LH_ItemCondition=1000&LH_FS=1&_udhi=5&prodch=0&_dmd=2&rt=nc'
dataList = []


class Data:

    def __init__(self, url="", info1="", info2="", info3="", info4=""):
        self.url = url
        self.info1 = info1
        self.info2 = info2
        self.info3 = info3
        self.info4 = info4
        print(url)
        print(info1)
        print(info2)
        print(info3)
        print(info4)


def parse(url):
    page = urllib.request.urlopen(url)
    result = page.read()
    soup = BeautifulSoup(result, 'html.parser')
    span1 = soup.find("span", class_="vi-qty-pur-lnk")
    span2 = soup.find("span", class_="mbg-nw")
    span3 = soup.find("span", class_="mbg-l")
    div = soup.find("div", id="si-fb")

    item = Data(url, span1.a.string, span2.string, span3.a.string, div.string)
    dataList.append(item)


def parse_home(url):
    page = urllib.request.urlopen(url)
    result = page.read()
    soup = BeautifulSoup(result, 'html.parser')
    ul = soup.find("ul", class_="b-list__items_nofooter")
    for li in ul.contents:
        try:
            url = li.div.div.div.a["href"]
            parse(url)
        except:
            item = Data(url, "出错啦，请手动添加这条")
            dataList.append(item)


def write_to_txt(list):
    with open("xyf.txt", "a+", encoding="utf-8") as file:
        for item in dataList:
            file.writelines("\n")
            file.writelines(item.url)
            file.writelines("\n")
            file.writelines(item.info1 + "\t" + item.info2 + "\t" + item.info3 + "\t" + item.info4)
            file.writelines("\n")


def write_to_excel(list):
    excel = xlwt.Workbook(encoding="utf-8")
    sheet = excel.add_sheet("xyf")
    for item in dataList:
        sheet.write(dataList.index(item), 1, item.url)
        sheet.write(dataList.index(item), 2, item.info1)
        sheet.write(dataList.index(item), 3, item.info2)
        sheet.write(dataList.index(item), 4, item.info3)
        sheet.write(dataList.index(item), 5, item.info4)
    excel.save("xyf.xls")


parse_home(addressHome)
write_to_excel(dataList)
