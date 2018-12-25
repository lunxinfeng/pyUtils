# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    book_name = scrapy.Field()  # 题目一级目录
    book_sub_name = scrapy.Field()  # 题目二级目录
    course_index = scrapy.Field()  # 题目三级目录
    prepos_b = scrapy.Field()  # 题目黑子
    prepos_w = scrapy.Field()  # 题目白子
    answers = scrapy.Field()  # 题目解答
    board_size = scrapy.Field()  # 题目路数
    black_first = scrapy.Field()  # 黑先白先  1表示黑先  0表示白先
    qtypename = scrapy.Field()  # 题目类型
    levelname = scrapy.Field()  # 题目等级
    status = scrapy.Field()  # 题目状态  1表示已淘汰
    title = scrapy.Field()  # 题目说明
    signs = scrapy.Field()  # 题目标记
    # type = scrapy.Field()  # 答案类型  1表示正确答案  2表示变化答案  3表示失败答案
    # s_type = scrapy.Field()  # 答案审核状态  1表示待审核  2表示已审核
