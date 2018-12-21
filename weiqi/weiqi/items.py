# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    book_name = scrapy.Field()
    book_sub_name = scrapy.Field()
    course_index = scrapy.Field()
    prepos_b = scrapy.Field()
    prepos_w = scrapy.Field()
    answers = scrapy.Field()
    board_size = scrapy.Field()
    black_first = scrapy.Field()
    qtypename = scrapy.Field()
    levelname = scrapy.Field()
