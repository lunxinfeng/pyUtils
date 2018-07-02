# -*- coding: utf-8 -*-
import scrapy


# https://www2.youku00.com/20180318/FHUvAKei/index.m3u8
# https://videos3.jsyunbf.com/2018/06/29/fOqRLvkVSQW3MjTf/out000.ts
def covert(a):
    if a >= 100:
        return str(a)
    elif a >= 10:
        return "0" + str(a)
    else:
        return "00" + str(a)


class ZhuboSpider(scrapy.Spider):
    name = 'zhubo'
    allowed_domains = ['meiwangle.com']
    start_urls = []

    base_url = "https://videos3.jsyunbf.com/2018/06/29/fOqRLvkVSQW3MjTf/"
    num = 188

    for i in range(0, num + 1):
        start_urls.append(base_url + "out" + covert(num) + ".ts")

    print(start_urls.__len__())

    def parse(self, response):
        pass


