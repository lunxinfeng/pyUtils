# -*- coding: utf-8 -*-
import json

import scrapy
from selenium import webdriver
from scrapy import Request
import re

from selenium.webdriver.chrome.options import Options
from weiqi.items import WeiqiItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.101weiqi.com']
    start_urls = ['https://www.101weiqi.com/book/level/1']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.quit()

    def start_requests(self):
        # start_urls = ['https://www.101weiqi.com/book/level/1']
        start_urls = ['https://www.101weiqi.com/book/shihuochidian/']
        # start_urls = ['https://www.101weiqi.com/book/tianlongtu/', "https://www.101weiqi.com/book/219/"]
        for url in start_urls:
            yield Request(url=url, callback=self.parse_2)

    def parse(self, response):
        """解析第一个页面，书的列表页"""
        url_list = response.css("a[ng-href*=book]::attr(href)").extract()
        url_list = [item for item in url_list if re.findall(r"([0-9]/)$", str(item)).__len__() > 0]
        base_url = "https://www.101weiqi.com"

        for item in url_list:
            yield Request(url=base_url + item, callback=self.parse_2)

    def parse_2(self, response):
        """分情况，有的书有二级目录，有的没有二级目录"""
        has_sub_page = True
        url_list = response.css(".node::attr(href)").extract()
        print("二级目录：" + str(url_list.__len__()))
        print(url_list)
        if url_list.__len__() == 0:
            has_sub_page = False
            url_list = response.css(".col-xs-6 a::attr(href)").extract()
        base_url = "https://www.101weiqi.com"
        if has_sub_page:
            for item in url_list:
                yield Request(url=base_url + item, callback=self.parse_22)
        else:
            for item in url_list:
                yield Request(url=base_url + item, callback=self.parse_3)

    def parse_22(self, response):
        """三级目录解析，有二级目录的情况下"""
        url_list = response.css(".questionitem a::attr(href)").extract()
        base_url = "https://www.101weiqi.com"
        print(url_list)
        # return Request(url=base_url + url_list[0], callback=self.parse_3)
        for item in url_list:
            yield Request(url=base_url + item, callback=self.parse_3)

    def parse_3(self, response):
        """解析最终的棋谱页面"""
        item = WeiqiItem()
        # print("result:" + str(response.body))
        # 获取标题相关信息
        book_name = response.xpath("//ul[contains(@class,'breadcrumb')][1]/li[1]/a/text()").get()
        print(book_name)
        book_sub_name = response.xpath("//ul[contains(@class,'breadcrumb')][1]/li[2]/a/text()").get()
        print(book_sub_name)
        course_index = response.xpath("//ul[contains(@class,'breadcrumb')][1]/li[3]/text()").get()
        print(course_index)

        # 获取棋谱相关信息
        scripts = response.css("script:contains('g_qq')::text").get()
        # print("result:" + str(scripts))

        list = re.findall(r"g_qq = ({.*?});var", str(scripts))
        chess_json = json.loads(list[0])

        title = chess_json['title']
        status = chess_json['status']
        prepos = chess_json['prepos']
        prepos_b = prepos[0]
        prepos_w = prepos[1]
        signs = chess_json['signs']
        answers = chess_json['answers']
        board_size = chess_json['lu']
        black_first = chess_json['blackfirst']
        if black_first:
            black_first = "1"
        else:
            black_first = "0"

        qtypename = chess_json['qtypename']
        levelname = chess_json['levelname']

        item["book_name"] = book_name
        item["book_sub_name"] = book_sub_name
        item["course_index"] = course_index
        item["prepos_b"] = prepos_b
        item["prepos_w"] = prepos_w
        item["answers"] = answers
        item["board_size"] = board_size
        item["black_first"] = black_first
        item["qtypename"] = qtypename
        item["levelname"] = levelname
        item["status"] = status
        item["title"] = "" if title.__len__() == 0 else title
        item["signs"] = signs
        yield item
